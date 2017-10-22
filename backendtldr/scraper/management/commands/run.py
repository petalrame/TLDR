from django.core.management.base import BaseCommand
from scraper import scraper_runner

class Command(BaseCommand):
    def handle(self, **options):
        scraper_runner.main()
