import logging
from django.core.management.base import BaseCommand, CommandError
import spendata.openx 

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    args = ''
    help = 'Loads Acxiom Data into the DB'

    def handle(self, *args, **options):
        try:
            # Connect and logon
            r = spendata.openx.OpenXDataRetriever()
            
            # Get parsers
            r.get_model_code()
            
            # Start saving!
            r.get_lookup_data()
            
        except Exception as e:
            logger.error("Error loading OpenX lookup data into the DB: %s" % str(e))
            raise CommandError("Error loading OpenX lookup data into the DB: %s" % str(e))


