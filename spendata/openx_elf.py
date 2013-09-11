import logging
import gzip
import csv
from cStringIO import StringIO

from spendata.models import ELFRequestData, ELFImpressionData, ELFClickData, ELFConversionData
from spendata.openx import OpenXDataRetriever

logger = logging.getLogger(__name__)

class ELFLogDialect(csv.Dialect):
    delimiter = '\t'
    quotechar = '"'
    doublequote = False
    skipinitialspace = False
    lineterminator = '\n'
    quoting = 0

# Which model to store each type of data in
ELFDATATYPE = {
    'request':    ELFRequestData,
    'click':      ELFClickData,
    'impression': ELFImpressionData
}

# Serial to start with if nothing in DB
ELF_FIRST_SERIAL = {
    'request': 112845,
    'click': 0,
    'impression': 0
}

# Conversion: 
# HTTPError: HTTP Error 404: ODFI failure: invalid range

# Click: 
# [ERROR] [openx_elf get_elf_data] Eventfeed for type click throws an error
# Traceback (most recent call last):
#   File "/Users/alex/Gramercy/spendometer/project/spendata/openx_elf.py", line 50, in get_elf_data
#     dataset = self.ox.get(url).get('dataset',[])
#   File "/Users/alex/.virtualenvs/spendometer/lib/python2.7/site-packages/ox3apiclient/__init__.py", line 285, in get
#     res = self.request(self._resolve_url(url), method='GET')
#   File "/Users/alex/.virtualenvs/spendometer/lib/python2.7/site-packages/ox3apiclient/__init__.py", line 152, in request
#     res = urllib2.urlopen(req)
#   File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/urllib2.py", line 126, in urlopen
#     return _opener.open(url, data, timeout)
#   File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/urllib2.py", line 400, in open
#     response = self._open(req, data)
#   File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/urllib2.py", line 418, in _open
#     '_open', req)
#   File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/urllib2.py", line 378, in _call_chain
#     result = func(*args)
#   File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/urllib2.py", line 1207, in http_open
#     return self.do_open(httplib.HTTPConnection, req)
#   File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/urllib2.py", line 1180, in do_open
#     r = h.getresponse(buffering=True)
#   File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/httplib.py", line 1030, in getresponse
#     response.begin()
#   File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/httplib.py", line 407, in begin
#     version, status, reason = self._read_status()
#   File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/httplib.py", line 371, in _read_status
#     raise BadStatusLine(line)
# BadStatusLine: ''

# Impression: 
# [DEBUG] [openx_elf get_elf_data] Requesting URL '/a/eventfeed?type=impression&range=0&format=json&pretty=true'
# [ERROR] [openx_elf get_elf_data] Eventfeed for type impression throws an error
# Traceback (most recent call last):
#   File "/Users/alex/Gramercy/spendometer/project/spendata/openx_elf.py", line 50, in get_elf_data
#     #   File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/urllib2.py", line 1207, in http_open
#   File "/Users/alex/.virtualenvs/spendometer/lib/python2.7/site-packages/ox3apiclient/__init__.py", line 285, in get
#     res = self.request(self._resolve_url(url), method='GET')
#   File "/Users/alex/.virtualenvs/spendometer/lib/python2.7/site-packages/ox3apiclient/__init__.py", line 159, in request
#     raise err
# HTTPError: HTTP Error 502: Bad Gateway


class ELFDataRetriever(OpenXDataRetriever):

    EVENT_URL = '/a/eventfeed?type={type}&range={serial}&format=json&pretty=true'

    def get_elf_data(self, datatype='request'):
        
        for datatype in ['request', 'click', 'impression']:
        
            serial = get_latest_serial(datatype)
            
            try:
                logger.info('Requesting eventfeed for type: {}, serial: {}'.format(datatype, serial))
                url = self.EVENT_URL.format(type=datatype, serial=serial)
                logger.debug('Requesting URL {!r}'.format(url))
                dataset = self.ox.get(url).get('dataset',[])
                
                if dataset:
                    logger.info('Eventfeed length: {}, ranges from serials {} to {}'.format(
                        len(dataset), 
                        dataset[-1].get('serial'),
                        dataset[0].get('serial')
                    ))
                else:
                    logger.warning('Eventfeed is empty')
                
            except Exception as e:
                logger.error('Eventfeed for type {} throws an error'.format(datatype))
                logger.exception(e)
                continue
            
            # Reverse order - oldest to newest
            for row in dataset[::-1]:
                logger.debug('Processing serial {}'.format(row.get('serial')))
                
                # Only unzip non-zero records
                if int(row['@recordCount']) == 0:
                    continue
                
                # TODO handle multiple parts? Why is this a dict?
                if not isinstance(row['parts'], dict):
                    raise NotImplementedError('Parts is not a dict')
                    
                filename = parse_filename(row['parts']['part']['@locator'])
                
                data = self.get_gzipped_data(filename)
                self.save_elf_data(data, row, datatype)
                

    def get_gzipped_data(self, url):
        data = self.ox.request(self.ox._resolve_url(url), method='GET')
        buf = StringIO(data.read())
        f = gzip.GzipFile(fileobj=buf)
        reader = csv.DictReader(f, dialect=ELFLogDialect)
        return list(reader)
        
    def save_elf_data(self, data, row, datatype):
        
        if int(row['@revision']) > 1:
            raise NotImplementedError('Revision incremented')
        
        for d in data:
            try:
                d['event_time']     = d.pop('#event_time') # #event_time -> event_time
                d['revision']       = row['@revision']
                d['serial_number']  = row['serial']
                d['part_id']        = row['parts']['part']['@id']
                
                # Remove empty items
                d = {k: v for k, v in d.iteritems() if v is not None and v != ''}
                
                # Get model for this datatype
                model = ELFDATATYPE[datatype]
                obj = model.objects.create(**d)
                
                logger.info('ELF data id {} saved'.format(obj.id))
            
            except KeyError as e:
                logger.exception(e)
                logger.info(d)
    

def parse_filename(filename):
    """ E.g. 'http://montavo-ui3.openxenterprise.com/ox/3.0/a/eventfeed/fetch?file=/blah.txt.gz' to -> /a/eventfeed/... """
    # TODO check
    pos = filename.find('/ox/3.0/a/') # should be ~38
    return filename[pos+7:]
    
    
def get_latest_serial(datatype):
    model = ELFDATATYPE[datatype]
    
    try:
        serial = model.objects.latest('pk').serial_number
    except model.DoesNotExist:
        serial = ELF_FIRST_SERIAL.get(datatype, 0)
        logger.warning('No serial for {}, starting at {}'.format(datatype, serial))
        
    return serial
    
# ELF_LOG_FIELDS = ['event_time',
#  'transaction_id',
#  'transaction_time',
#  'user_id',
#  'user_id_new',
#  'publisher_id',
#  'site_id',
#  'ad_unit_id',
#  'ad_unit_grp_id',
#  'ad_width',
#  'ad_height',
#  'delivery_medium_id',
#  'site_section_id',
#  'content_type_id',
#  'content_topic_id',
#  'screen_location_id',
#  'advertiser_id',
#  'order_id',
#  'line_item_id',
#  'ad_id',
#  'is_companion',
#  'is_auto_refresh',
#  'is_fallback_ad',
#  'is_pre_fetch',
#  'user_ip_address',
#  'user_latitude',
#  'user_longitude',
#  'user_continent',
#  'user_country',
#  'user_state',
#  'user_dma',
#  'user_msa',
#  'user_city',
#  'user_zip',
#  'user_connection_speed',
#  'user_connection_type',
#  'user_device',
#  'mobile_carrier',
#  'mobile_net_type',
#  'user_screen_res',
#  'user_agent',
#  'browser_name',
#  'browser_version',
#  'user_operating_system',
#  'user_os_version',
#  'browser_language',
#  'page_url',
#  'referrer_url',
#  'matched_targeting',
#  'custom_fields',
#  'audience_segments',
#  'traffic_rejected']
#       
#       
# # Sample log data:
# [{'ad_height': '50',
#   'ad_id': '1175352',
#   'ad_unit_grp_id': '',
#   'ad_unit_id': '416409',
#   'ad_width': '320',
#   'advertiser_id': '115196',
#   'audience_segments': '',
#   'browser_language': 'en-us',
#   'browser_name': 'Other',
#   'browser_version': '',
#   'content_topic_id': '',
#   'content_type_id': '99',
#   'custom_fields': 'channel=coffeeshop',
#   'delivery_medium_id': 'DMID.MOBILE',
#   'event_time': '2013-09-10 04:58:02',
#   'is_auto_refresh': 'false',
#   'is_companion': 'false',
#   'is_fallback_ad': 'false',
#   'is_pre_fetch': 'false',
#   'line_item_id': '701683',
#   'matched_targeting': '',
#   'mobile_carrier': '',
#   'mobile_net_type': '',
#   'order_id': '208567',
#   'page_url': '',
#   'publisher_id': '115194',
#   'referrer_url': '',
#   'screen_location_id': '',
#   'site_id': '86413',
#   'site_section_id': '',
#   'traffic_rejected': 'false',
#   'transaction_id': 'fc66414c-0b05-448b-a859-b915734c789c',
#   'transaction_time': '2013-09-10 04:58:02',
#   'user_agent': 'MontavoPTG/1.0 CFNetwork/609.1.4 Darwin/12.4.0',
#   'user_city': 'hyderabad',
#   'user_connection_speed': 'medium',
#   'user_connection_type': 'fixed wireless',
#   'user_continent': 'asia',
#   'user_country': 'in',
#   'user_device': '',
#   'user_dma': '',
#   'user_id': '9bdc1e8a-38aa-0ded-4d15-61c32cde9fe1',
#   'user_id_new': 'false',
#   'user_ip_address': '183.82.48.194',
#   'user_latitude': '17.385',
#   'user_longitude': '78.487',
#   'user_msa': '',
#   'user_operating_system': 'Other',
#   'user_os_version': '',
#   'user_screen_res': '',
#   'user_state': 'andhra pradesh',
#   'user_zip': '500000'},
# ]  

# {u'@dataSize': u'352',
#  u'@id': u'25819516',
#  u'@recordCount': u'0',
#  u'@revision': u'1',
#  u'@status': u'READY',
#  u'dateCreated': u'2013-09-10 09:00:11 UTC',
#  u'endTimestamp': u'2013-09-10 07:59:00 UTC',
#  u'feed': {u'@id': u'223',
#   u'@name': u'5295476f-cc8f-492d-a748-305882e65e47_ox_request_log_minutely'},
#  u'parts': {u'part': {u'@compressionType': u'GZIP',
#    u'@dataSize': u'352',
#    u'@digest': u'498b8331dcfa44c55d5980a6ead8a218',
#    u'@gzipped': u'true',
#    u'@id': u'25753213',
#    u'@index': u'1',
#    u'@locator': u'http://montavo-ui3.openxenterprise.com/ox/3.0/a/eventfeed/fetch?file=/5295476f-cc8f-492d-a748-305882e65e47/ox_request_log_minutely/2013-09/requests_v4_2013-09-10_07-58_5295476f-cc8f-492d-a748-305882e65e47.txt.gz',
#    u'@recordCount': u'0'}},
#  u'readableInterval': u'2013-09-10_07:58:00',
#  u'schema': {u'@locator': u'http://montavo-ui3.openxenterprise.com/ox/3.0/a/eventfeed/schema?version=4&name=OX_EventLog',
#   u'@name': u'OX_EventLog',
#   u'@version': u'4'},
#  u'serial': u'112769',
#  u'startTimestamp': u'2013-09-10 07:58:00 UTC'}

    # ZIPPED ELF feeds
    # http://stackoverflow.com/questions/3947120/does-python-urllib2-will-automaticly-uncompress-gzip-data-from-fetch-webpage

    # we need
    # 1. Stores (which are Advertisers from OpenX viewpoint) [All accounts with Account Type=6 in current implementation]
    # 2. Campaigns [Orders + Order Line Items + Creatives]
    # 3. Advertisements [All ads within campaign window]
    # 4. ELF [Performance basis ads]
