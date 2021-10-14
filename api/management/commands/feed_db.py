from django.core.management.base import BaseCommand, CommandError

from api.db import DatabaseManager


class Command(BaseCommand):
    help = "Feed the database. Private function, it is a cronjob"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        db_manager = DatabaseManager()
        try:
            db_manager.load_dump()
        except Exception as e:
            raise CommandError(f'Error trying feed the database.\n{e}')
