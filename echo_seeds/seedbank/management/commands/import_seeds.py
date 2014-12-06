from django.core.management.base import BaseCommand
from utils.importers import seed_data


class Command(BaseCommand):
    args = None
    help = "Imports seed data from csv."

    def handle(self, *args, **options):

        seed_data.write()
