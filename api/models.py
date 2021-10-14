import datetime
import logging
from django.db import models
from django.core.exceptions import FieldDoesNotExist
from api.custom_models import ListField, StatusField

logger = logging.getLogger(__name__)


class Product(models.Model):
    """Product model."""

    code = models.TextField(default=None, null=True, db_index=True)
    url = models.TextField(default=None, null=True)
    creator = models.TextField(default=None, null=True)
    created_t = models.IntegerField(default=None, null=True)
    created_datetime = models.DateTimeField(default=None, null=True)
    last_modified_t = models.IntegerField(default=None, null=True)
    last_modified_datetime = models.DateTimeField(default=None, null=True)
    product_name = models.TextField(default=None, null=True)
    generic_name = models.TextField(default=None, null=True)
    quantity = models.TextField(default=None, null=True)
    imported_t = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=9, choices=StatusField.choices, default=StatusField.DRAFT
    )

    packaging = ListField(default=None, null=True)
    packaging_tags = ListField(default=None, null=True)
    brands = ListField(default=None, null=True)
    brands_tags = ListField(default=None, null=True)
    categories = ListField(default=None, null=True)
    categories_tags = ListField(default=None, null=True)
    categories_fr = ListField(default=None, null=True)
    origins = ListField(default=None, null=True)
    origins_tags = ListField(default=None, null=True)
    manufacturing_places = ListField(default=None, null=True)
    manufacturing_places_tags = ListField(default=None, null=True)
    labels = ListField(default=None, null=True)
    labels_tags = ListField(default=None, null=True)
    labels_fr = ListField(default=None, null=True)
    emb_codes = models.TextField(default=None, null=True)
    emb_codes_tags = ListField(default=None, null=True)
    first_packaging_code_geo = ListField(default=None, null=True)
    cities = ListField(default=None, null=True)
    cities_tags = ListField(default=None, null=True)
    purchase_places = ListField(default=None, null=True)
    stores = ListField(default=None, null=True)
    countries = ListField(default=None, null=True)
    countries_tags = ListField(default=None, null=True)
    countries_fr = ListField(default=None, null=True)

    ingredients_text = ListField(default=None, null=True)
    traces = ListField(default=None, null=True)
    traces_tags = ListField(default=None, null=True)


    additives = ListField(default=None, null=True)
    additives_n = models.IntegerField(default=None, null=True)
    additives_tags = ListField(default=None, null=True)
    image_small_url = models.TextField(default=None, null=True)
    image_url = models.TextField(default=None, null=True)
    ingredients_from_palm_oil = ListField(default=None, null=True)
    ingredients_from_palm_oil_n = models.IntegerField(default=None, null=True)
    ingredients_from_palm_oil_tags = ListField(default=None, null=True)
    ingredients_that_may_be_from_palm_oil = ListField(default=None, null=True)
    ingredients_that_may_be_from_palm_oil_n = models.IntegerField(
        default=None, null=True
    )
    ingredients_that_may_be_from_palm_oil_tags = ListField(default=None, null=True)
    main_category = models.TextField(default=None, null=True)
    main_category_fr = models.TextField(default=None, null=True)
    no_nutriments = models.TextField(default=None, null=True)
    nutrition_grade_fr = models.CharField(max_length=1, default=None, null=True)
    serving_size = models.TextField(default=None, null=True)

    _alpha_linolenic_acid_100g = models.FloatField(default=None, null=True)
    _arachidic_acid_100g = models.FloatField(default=None, null=True)
    _arachidonic_acid_100g = models.FloatField(default=None, null=True)
    _behenic_acid_100g = models.FloatField(default=None, null=True)
    _butyric_acid_100g = models.FloatField(default=None, null=True)
    _capric_acid_100g = models.FloatField(default=None, null=True)
    _caproic_acid_100g = models.FloatField(default=None, null=True)
    _caprylic_acid_100g = models.FloatField(default=None, null=True)
    _cerotic_acid_100g = models.FloatField(default=None, null=True)
    _dihomo_gamma_linolenic_acid_100g = models.FloatField(default=None, null=True)
    _docosahexaenoic_acid_100g = models.FloatField(default=None, null=True)
    _eicosapentaenoic_acid_100g = models.FloatField(default=None, null=True)
    _elaidic_acid_100g = models.FloatField(default=None, null=True)
    _erucic_acid_100g = models.FloatField(default=None, null=True)
    _fructose_100g = models.FloatField(default=None, null=True)
    _gamma_linolenic_acid_100g = models.FloatField(default=None, null=True)
    _glucose_100g = models.FloatField(default=None, null=True)
    _gondoic_acid_100g = models.FloatField(default=None, null=True)
    _lactose_100g = models.FloatField(default=None, null=True)
    _lauric_acid_100g = models.FloatField(default=None, null=True)
    _lignoceric_acid_100g = models.FloatField(default=None, null=True)
    _linoleic_acid_100g = models.FloatField(default=None, null=True)
    _maltodextrins_100g = models.FloatField(default=None, null=True)
    _maltose_100g = models.FloatField(default=None, null=True)
    _mead_acid_100g = models.FloatField(default=None, null=True)
    _melissic_acid_100g = models.FloatField(default=None, null=True)
    _montanic_acid_100g = models.FloatField(default=None, null=True)
    _myristic_acid_100g = models.FloatField(default=None, null=True)
    _nervonic_acid_100g = models.FloatField(default=None, null=True)
    _oleic_acid_100g = models.FloatField(default=None, null=True)
    _palmitic_acid_100g = models.FloatField(default=None, null=True)
    _stearic_acid_100g = models.FloatField(default=None, null=True)
    _sucrose_100g = models.FloatField(default=None, null=True)
    alcohol_100g = models.FloatField(default=None, null=True)
    beta_carotene_100g = models.FloatField(default=None, null=True)
    beta_glucan_100g = models.FloatField(default=None, null=True)
    bicarbonate_100g = models.FloatField(default=None, null=True)
    biotin_100g = models.FloatField(default=None, null=True)
    caffeine_100g = models.FloatField(default=None, null=True)
    calcium_100g = models.FloatField(default=None, null=True)
    carbohydrates_100g = models.FloatField(default=None, null=True)
    carbon_footprint_100g = models.FloatField(default=None, null=True)
    carnitine_100g = models.FloatField(default=None, null=True)
    casein_100g = models.FloatField(default=None, null=True)
    chloride_100g = models.FloatField(default=None, null=True)
    chlorophyl_100g = models.FloatField(default=None, null=True)
    cholesterol_100g = models.FloatField(default=None, null=True)
    choline_100g = models.FloatField(default=None, null=True)
    chromium_100g = models.FloatField(default=None, null=True)
    cocoa_100g = models.FloatField(default=None, null=True)
    collagen_meat_protein_ratio_100g = models.FloatField(default=None, null=True)
    copper_100g = models.FloatField(default=None, null=True)
    energy_100g = models.FloatField(default=None, null=True)
    energy_from_fat_100g = models.FloatField(default=None, null=True)
    fat_100g = models.FloatField(default=None, null=True)
    fiber_100g = models.FloatField(default=None, null=True)
    fluoride_100g = models.FloatField(default=None, null=True)
    folates_100g = models.FloatField(default=None, null=True)
    fruits_vegetables_nuts_100g = models.FloatField(default=None, null=True)
    glycemic_index_100g = models.FloatField(default=None, null=True)
    inositol_100g = models.FloatField(default=None, null=True)
    iodine_100g = models.FloatField(default=None, null=True)
    iron_100g = models.FloatField(default=None, null=True)
    magnesium_100g = models.FloatField(default=None, null=True)
    manganese_100g = models.FloatField(default=None, null=True)
    molybdenum_100g = models.FloatField(default=None, null=True)
    monounsaturated_fat_100g = models.FloatField(default=None, null=True)
    nucleotides_100g = models.FloatField(default=None, null=True)
    nutrition_score_fr_100g = models.FloatField(default=None, null=True)
    nutrition_score_uk_100g = models.FloatField(default=None, null=True)
    omega_3_fat_100g = models.FloatField(default=None, null=True)
    omega_6_fat_100g = models.FloatField(default=None, null=True)
    omega_9_fat_100g = models.FloatField(default=None, null=True)
    pantothenic_acid_100g = models.FloatField(default=None, null=True)
    ph_100g = models.FloatField(default=None, null=True)
    phosphorus_100g = models.FloatField(default=None, null=True)
    phylloquinone_100g = models.FloatField(default=None, null=True)
    polyols_100g = models.FloatField(default=None, null=True)
    polyunsaturated_fat_100g = models.FloatField(default=None, null=True)
    potassium_100g = models.FloatField(default=None, null=True)
    proteins_100g = models.FloatField(default=None, null=True)
    salt_100g = models.FloatField(default=None, null=True)
    saturated_fat_100g = models.FloatField(default=None, null=True)
    selenium_100g = models.FloatField(default=None, null=True)
    serum_proteins_100g = models.FloatField(default=None, null=True)
    silica_100g = models.FloatField(default=None, null=True)
    sodium_100g = models.FloatField(default=None, null=True)
    starch_100g = models.FloatField(default=None, null=True)
    sugars_100g = models.FloatField(default=None, null=True)
    taurine_100g = models.FloatField(default=None, null=True)
    trans_fat_100g = models.FloatField(default=None, null=True)
    vitamin_a_100g = models.FloatField(default=None, null=True)
    vitamin_b12_100g = models.FloatField(default=None, null=True)
    vitamin_b1_100g = models.FloatField(default=None, null=True)
    vitamin_b2_100g = models.FloatField(default=None, null=True)
    vitamin_b6_100g = models.FloatField(default=None, null=True)
    vitamin_b9_100g = models.FloatField(default=None, null=True)
    vitamin_c_100g = models.FloatField(default=None, null=True)
    vitamin_d_100g = models.FloatField(default=None, null=True)
    vitamin_e_100g = models.FloatField(default=None, null=True)
    vitamin_k_100g = models.FloatField(default=None, null=True)
    vitamin_pp_100g = models.FloatField(default=None, null=True)
    zinc_100g = models.FloatField(default=None, null=True)

    def __str__(self) -> str:
        return f"{self.product_name}"

    @classmethod
    def parse_api_fields(self, data):
        """
        Parse API fields and return a django ORM ready dict
        """
        treated_fields = {}
        for field in data.keys():
            django_field = field.replace("-", "_")

            value = (data.get(field) or "").strip()

            try:
                field_class = self._meta.get_field(django_field).__class__
            except FieldDoesNotExist:
                # logger.info("A field type that shouldn't exists has been added : %s" % field)
                continue

            if value == "":
                value = None
            elif field_class == models.FloatField:
                try:
                    value = float(value)
                except ValueError:
                    logger.debug(
                        "Value %s could not be converted to float. Using none, intead"
                        % (value)
                    )
                finally:
                    value = None
            elif field_class == models.IntegerField:
                try:
                    value = int(value)
                except ValueError:
                    logger.debug(
                        "Value %s could not be converted to int. Using none, intead"
                        % (value)
                    )
                finally:
                    value = None
            elif field_class == models.DateTimeField:
                value = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")
            elif field_class == ListField:
                if " ] [ " in value:
                    value = value.strip("[ ").strip(" ]").split("] [")
                elif ", " in value:
                    value = value.split(", ")
                else:
                    value = value.split(",")

            treated_fields[django_field] = value

        return treated_fields

    @classmethod
    def load(self, data, create=False):
        """
        Create an Product instance from a dict or return updated existing instance.
        :param data: dict serialization coming from dump
        """
        treated_fields = self.parse_api_fields(data)

        if create:
            instance = self.objects.create(**treated_fields)
        else:
            instances = self.objects.filter(code=treated_fields.get("code", ""))
            if instances.count() == 0:
                raise Exception(
                    "Object update requested but not in DB, use create=True. %s" % data
                )

            instances.update(**treated_fields)
            instance = instances.first()

        return instance
