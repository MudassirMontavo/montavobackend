# retrieve ELF file list
# http://www.openx.com/docs/openx_help_center/content/event_feeds_retrievinglist.html

import ox3apiclient

email = "montavotestacct@outlook.com"
password = "!M0ntav0!"
domain = "http://montavo-ui3.openxenterprise.com"
realm = "montavo_ad_server"
consumer_key = "1a81f2a240f1c3bf78af1353200c9839cb3cad91"
consumer_secret = "30650b5112c2d6050732c90e74b57e0a01c28212"

ox = ox3apiclient.Client(
    email=email,
    password=password,
    domain=domain,
    realm=realm,
    consumer_key=consumer_key,
    consumer_secret=consumer_secret)

ox.logon(email, password)

ac = ox.get('/a/account')

ac = ox.get('/a/eventfeed?type=request&range=0&format=json&pretty=true')
