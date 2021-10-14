from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from api.custom_models import StatusField
from api.models import Product
from api.serializers import ProductSerializer
from rest_framework import viewsets


class ProductViewSet(viewsets.ModelViewSet):
    """
    Product viewset.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def destroy(self, request, pk):
        product = self.get_object(pk)
        product.status = StatusField.TRASH
        product.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
