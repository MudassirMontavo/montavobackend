import logging
from django.core.management.base import BaseCommand, CommandError
import spendata.acxiom

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    args = ''
    help = 'Loads Acxiom Data into the DB'

    def handle(self, *args, **options):
        try:
            spendata.acxiom.AcxiomDataReader().read_into_db()
        except Exception, err:
            logger.error("Error loading Acxiom Data into the DB: %s" % str(err))
            raise CommandError("Error loading Acxiom Data into the DB: %s" % str(err))


