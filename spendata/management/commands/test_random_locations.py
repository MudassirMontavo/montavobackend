import logging
from django.core.management.base import BaseCommand, CommandError
import spendata.home_circle 
from spendata.models import MobileAppMobileData

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    args = ''
    help = "Generates 1000 random coordinates for user 'test'"

    def handle(self, *args, **options):
        try:            
            
            spendata.home_circle.generate_random_data()
            
        except Exception as e:
            logger.error("Error loading OpenX lookup data into the DB: %s" % str(e))
            raise CommandError("Error loading OpenX lookup data into the DB: %s" % str(e))
