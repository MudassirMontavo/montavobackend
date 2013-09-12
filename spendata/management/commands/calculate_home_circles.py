import logging
from django.core.management.base import BaseCommand, CommandError
import spendata.home_circle 
from spendata.models import MobileAppMobileData

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    args = ''
    help = "Calculates every user's home circle"

    def handle(self, *args, **options):
        try:
            
            for user in MobileAppMobileData.objects.all().values('user_id'):
                user_id = user['user_id']
                logger.info('Calculating home circle for user: {}'.format(user_id))
                spendata.home_circle.save_home_circle(user_id)
            
        except Exception as e:
            logger.error("Error calculating users home circles: %s" % str(e))
            raise CommandError("Error calculating users home circles: %s" % str(e))
