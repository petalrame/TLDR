from django.core.management.base import BaseCommand
import sys
sys.path.append('/Users/sam/Documents/projects/TLDR/backendtldr/scraper')
import scraper_runner

class Command(BaseCommand):
    def handle(self, **options):
        scraper_runner.main()