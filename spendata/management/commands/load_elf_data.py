import logging
from django.core.management.base import BaseCommand, CommandError
from spendata.openx_elf import ELFDataRetriever 

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    args = ''
    help = 'Loads Acxiom Data into the DB'

    def handle(self, *args, **options):
        try:
            # Connect and logon
            r = ELFDataRetriever()
            
            # Start saving!
            r.get_elf_data()
            
        except Exception as e:
            logger.error("Error loading OpenX ELF data into the DB: %s" % str(e))
            raise CommandError("Error loading OpenX ELF data into the DB: %s" % str(e))


