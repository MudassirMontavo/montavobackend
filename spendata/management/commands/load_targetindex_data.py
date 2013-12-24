import logging
from django.core.management.base import BaseCommand, CommandError
# from spendata.openx_elf import ELFDataRetriever
from django.db import connection, transaction

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    args = ''
    help = 'Loads Acxiom Data into the DB'

    def handle(self, *args, **options):
        try:
           cursor = connection.cursor()
           cursor.execute("""insert into spendata_openxadtargetingindex(ad_id, account_id, lineitem_id, latitude, longitude, title, offer, targeting) select ox_ad.id as ad_id, ox_ad.account_id as account_id, ox_ad.lineitem_id as lineitem_id, latitude, longitude, ox_ad.name as title, 'Offer Text' as Offer , ox_li.oxtl as targeting from spendata_openxad ox_ad join spendata_acxiombdfprimary ac_bp  ON cast(ox_ad.account_id as text) = ac_bp.openx_account_id join spendata_openxlineitem ox_li ON ox_li.id = ox_ad.lineitem_id""")
           cursor.execute("commit")
        except Exception as e:
           logger.error("Error loading Targeting data into the DB: %s" % str(e))
           raise CommandError("Error loading Targeting Index data into the DB: %s" % str(e))
