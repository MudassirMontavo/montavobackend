# retrieve ELF file list
# http://www.openx.com/docs/openx_help_center/content/event_feeds_retrievinglist.html

import re
import logging
import ox3apiclient

logger = logging.getLogger(__name__)

email = "montavotestacct@outlook.com"
password = "!M0ntav0!"
domain = "montavo-ui3.openxenterprise.com"
realm = "montavo_ad_server"
consumer_key = "1a81f2a240f1c3bf78af1353200c9839cb3cad91"
consumer_secret = "30650b5112c2d6050732c90e74b57e0a01c28212"

class OpenXDataRetriever(object):


    def __init__(self):
        self.ox = ox3apiclient.Client(
            email=email,
            password=password,
            domain=domain,
            realm=realm,
            consumer_key=consumer_key,
            consumer_secret=consumer_secret)

        self.ox.logon(email, password)

        logger.info('OX Logon')

    def get_lookup_data(self):
        
        # gets the account ids
        logger.info('Calling /a/account')
        account_ids = self.ox.get('/a/account')
        
        logger.info('Account ids retrieved: {}'.format(len(account_ids)))
        
        for account_id in account_ids[:1]:
            logger.info('Calling /a/account/{}'.format(account_id))
            data = self.ox.get('/a/account/{}'.format(account_id))
            
            self.save_account_data(data)
    
    def save_account_data(self, data):
        logger.info('Saving data for account id: {}'.format(data.get('account_id')))
        
        
        
    
    def get_model_code(self):

        # OpenX datatypes we're interested in - e.g. account: /a/account/123 
        DATA_TYPES = ['account', 'user', 'role', 'site', 'adunit', 'adunitgroup', 'order',
            'lineitem', 'ad', 'creative', 'rule', 'report']

        # Data field types - e.g. string: TextField
        textfield = ('TextField', 'null=True')
        FIELD_TYPES = {
            'int':        ('IntegerField', 'null=True'),
            'bigint':     ('BigIntegerField', 'null=True'),
            'string':     textfield,
            'datetime':   ('DateTimeField', ''),
            'timestamp':  ('DateTimeField', ''),
            'varchar':    textfield,
            'varbinary':  textfield,
            'mediumtext': textfield,
            'email':      textfield,
            'ids':        textfield, # ??
            'url':        textfield,
            'decimal':    ('DecimalField', 'max_digits={}, decimal_places={}')
        }

        for name in DATA_TYPES:
            print '\n\nclass OpenX{}(models.Model):'.format(name.capitalize())
            
            fields = self.ox.get('/a/{name}/availableFields?action=create'.format(name=name))
            
            for field_name, field_data in fields.iteritems():
                                
                field_data_type = strip_brackets(field_data['type'])
                
                field_type, field_options = FIELD_TYPES.get(field_data_type, (None, None))
                
                # Unknown field type
                if field_type is None:
                    print 'MISSING FIELD TYPE: {} {}'.format(field_name, field_data)
                    continue
                
                # Decimal field (fixed decimal precision)
                if field_data_type == 'decimal':                    
                    one, two = field_data['type'].replace('decimal(', '').replace(')','').split(',')
                    field_options = field_options.format(one, two)
                
                print '    {field_name:<25} = models.{field_type}({options})'.format(
                    field_name = field_name,
                    field_type = field_type,
                    options =    field_options
                )
                


def strip_brackets(field):
    """ Strips out brackets and numbers - e.g. varchar(200) -> varchar, decimal(20,5) -> decimal"""
    try:
        return re.match('(.+)\(\d+,{0,1}\d*\)', field).groups()[0]
    except AttributeError:
        return field
    

# 
# 
# # get the associated data as well
# ox.get('/a/adunit?overload=medium')
# 
# # get the associated data as well
# ox.get('/a/adunit?overload=medium')
# 
# # what are the fields that need to be filled for create requests
# ox.get('/a/account/availableFields?action=create')

# Account
# [Note]  Note
# OpenX limits account objects to approximately 10k.

# User
# Role
# Site
# AdUnit
# AdUnitGroup
# SiteSection
# Order
# LineItem
# Ad
# Creative
# Rule
# Report



## ELF DATA:
#
# EVENT_URL = '/a/eventfeed?type={request_type}&range=0&format=json&pretty=true'
# 
# def get_request_data(self):
#     data = self.get(self.EVENT_URL.format(request_type='request'))
# 
# 
# def get_impression_data(self):
#     data = self.ox.get(self.EVENT_URL.format(request_type='request'))

# ZIPPED ELF feeds
# http://stackoverflow.com/questions/3947120/does-python-urllib2-will-automaticly-uncompress-gzip-data-from-fetch-webpage

# we need
# 1. Stores (which are Advertisers from OpenX viewpoint) [All accounts with Account Type=6 in current implementation]
# 2. Campaigns [Orders + Order Line Items + Creatives]
# 3. Advertisements [All ads within campaign window]
# 4. ELF [Performance basis ads]