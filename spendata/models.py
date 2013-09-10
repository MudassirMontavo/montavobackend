from django.db import models

ACXIOM_FIELD_MAPPING = {
    'DisplayName': 'display_name',
    'BusinessName': 'business_name',
    'Corporate Name': 'corporate_name',
    'StreetNumber': 'street_number',
    'StreetDirectional': 'street_directional',
    'StreetName': 'street_name',
    'StreetSuffix': 'street_suffix',
    'PostDirectional': 'post_directional',
    'UnitDesignator': 'unit_designator',
    'UnitNumber': 'unit_number',
    'CityName': 'city_name', 
    'StateCode': 'state_code',
    'Zip': 'zip_code',
    'Latitude': 'latitude',
    'Longitude': 'longitude',
    }

class AcxiomData(models.Model):
    display_name = models.TextField(blank=True)
    business_name = models.TextField(blank=True)
    corporate_name = models.TextField(blank=True)
    street_number = models.TextField(blank=True)
    street_directional = models.TextField(blank=True)
    street_name = models.TextField(blank=True)
    street_suffix = models.TextField(blank=True)
    post_directional = models.TextField(blank=True)
    unit_designator = models.TextField(blank=True)
    unit_number = models.TextField(blank=True)
    city_name = models.TextField(blank=True)
    state_code = models.TextField(blank=True)
    zip_code = models.TextField(null=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __unicode__(self):
        return self.business_name

class MobileAppUserData(models.Model):
    user_id = models.TextField(blank=True)
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    mobile_number = models.TextField(blank=True)
    gender = models.TextField(blank=True)
    user_city = models.TextField(blank=True)
    user_state = models.TextField(blank=True)
    user_zip = models.IntegerField(null=True, blank=True)
    user_country = models.TextField(blank=True)
    user_email = models.TextField(blank=True)
    income_range = models.TextField(blank=True)
    age_range = models.TextField(blank=True)
    area_code = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.user_id

class MobileAppMobileData(models.Model):
    user_data = models.ForeignKey('MobileAppUserData', blank=True, null=True, related_name='mobile_data')
    user_id = models.TextField(blank=True)
    device_id = models.TextField(blank=True)
    wireless_carrier = models.TextField(blank=True)
    device_manufacturer = models.TextField(blank=True)
    device_model = models.TextField(blank=True)

    def __unicode__(self):
        return self.device_id

class MobileAppLocationData(models.Model):
    device_data = models.ForeignKey('MobileAppMobileData', blank=True, null=True, related_name='location_data')
    device_id = models.TextField(blank=True)
    user_latitude = models.FloatField(null=True, blank=True)
    user_longitude = models.FloatField(null=True, blank=True)
    capture_time_utc = models.DateTimeField(null=True, blank=True)
 
    def __unicode__(self):
        return self.capture_time_utc

class ELFSerial(models.Model):
    created = models.DateTimeField(editable=False, auto_now_add=True)
    serial = models.BigIntegerField(blank=True, null=True, default=0)

class ELFDataRequestImpressionClick(models.Model):
    EVENT_CHOICES = (
        ('R', 'request'),
        ('I', 'impression'),
        ('C', 'click'),
    )
    event_type = models.CharField(max_length=1, choices=EVENT_CHOICES,
            blank=True, default = 'R')

    event_time = models.DateTimeField(null=True, blank=True, 
        help_text="""The date and time of the actual ad serving event, using the format: 
YYYYMM-DD hh:mm:ss. For example: 2011-02-28 12:45:30""")
    transaction_id = models.TextField(blank=True,
        help_text="""The unique ID for the original request event; OpenX generates this ID
for the request event, and includes this in feeds for subsequent related
events. For example: f0e6cd54-7232-4db5-8b25-c4ad7fdea840""")
    transaction_time = models.DateTimeField(null=True, blank=True, 
        help_text="""The date and time of the original request event, to which this ad serving
event is tied, using the format: YYYY-MM-DD hh:mm:ss. For example:
2011-02-28 12:45:30 (so, in the case of a request event, this time is
the same as the event_time).""")
    user_id = models.TextField(blank=True,
        help_text="""The unique ID for the user; OpenX generates this ID and tracks it
through request events. For example: 49be9663-ab0c-4af6-a1b1-
c9e357f523bd""")
    user_id_new = models.BooleanField(blank=True, default=False,
        help_text="""Indicates if OpenX generated the user ID on this request (True), or if it
originated in a separate request event (False).""")
    publisher_id = models.TextField(blank=True,
        help_text="""The unique ID of the publisher account that the ad inventory, which is
associated with this ad serving event, belongs to. For example: 25""")
    site_id  = models.IntegerField(null=True, blank=True,
        help_text="""The unique ID of the site associated with the ad serving event. For
example: 342""")
    ad_unit_id = models.IntegerField(null=True, blank=True,
        help_text="""The unique ID of the ad unit associated with the ad serving event. For
example: 3302""")
    ad_unit_grp_id = models.TextField(blank=True,
        help_text="""The unique ID of the ad unit group, if any, associated with the ad serving event. For example: 3492""")
    ad_width = models.IntegerField(null=True, blank=True,
        help_text="""The width dimension for the ad space associated with the ad serving event.""")
    ad_height = models.IntegerField(null=True, blank=True,
        help_text="""The height dimension for the ad space associated with the ad serving event""")
    page_id  = models.IntegerField(null=True, blank=True,
        help_text="""The unique ID of the ad unit group, if any, associated with the ad serving
event. For example: 3492""")
    delivery_medium_id = models.TextField(blank=True,
        help_text="""The ID for the delivery medium of the event. For example: DMID.WEB,
DMID.EMAIL DMID.LINEARVIDEO, DMID.NONLINEARVIDEO,
DMID.VIDEOCOMPANION, DMID.OVERLAYVIDEO, or DMID.VIDEO""")
    site_section_id = models.IntegerField(null=True, blank=True,
        help_text="""The ID for the section of the site where the ad inventory, which is
associated with this ad serving event, resides. For example: 847""")
    content_type_id = models.IntegerField(null=True, blank=True,
        help_text="""The ID for the content type assigned to the ad inventory, which is
associated with this ad serving event. For example: 99""")
    content_topic_id = models.TextField(blank=True,
        help_text="""A comma-delimited list of content topic IDs for the ad inventory associated
with this ad serving event. For example: 3425""")
    screen_location_id = models.TextField(blank=True,
        help_text="""The ID for the screen location of the ad inventory associated with the ad
serving event. For example: 785""")
    advertiser_id = models.IntegerField(null=True, blank=True,
        help_text="""The ID for the advertiser account whose ad serves to the ad inventory
associated with the ad serving event. For example: 56309""")
    order_id = models.IntegerField(null=True, blank=True,
        help_text="""The ID for the order associated with the ad serving event. For example:
876""")
    line_item_id = models.IntegerField(null=True, blank=True,
        help_text="""The ID for the line item associated with the ad serving event. For
example: 4389""")
    ad_id = models.IntegerField(null=True, blank=True,
        help_text="""The ID for the ad associated with the ad serving event. For example:
6732""")
    is_companion = models.BooleanField(blank=True, default=False,
        help_text="""Indicates whether or not the selected ad is a secondary ad in a
companion delivery situation. In the case of companion ad delivery, this is
True if the ad is not delivered to the master ad unit, or False if the ad is
delivered to the master ad unit.""")
    is_auto_refresh = models.BooleanField(blank=True, default=False,
        help_text="""Indicates whether or not the ad serving event is based on the auto-refresh
of an ad tag. This is True if the ad serving event is based on the autorefresh of an ad tag, or False if the ad serving event is not based in the
auto-refresh of an ad tag.""")
    is_fallback_ad = models.BooleanField(blank=True, default=False,
        help_text="""Indicates whether or not the ad serving event is related to a fallback
mechanism; that is, due to a lack of media support (e.g., no flash
support). This is True if the ad serving event is related to a fallback
mechanism, or False if the ad serving event is not related to a fallback
mechanism.""")
    is_pre_fetch = models.BooleanField(blank=True, default=False,
        help_text="""Indicates whether or not X-moz: prefetch is present in the HTTP
header. This is True if it is included in the header, or False if it is not
included in the header.""")
    user_ip_address = models.TextField(blank=True,
        help_text="""The IP address of the end-user associated with the ad serving event.""")
    user_latitude = models.FloatField(null=True, blank=True,
        help_text="""The latitude coordinate of the end-user associated with the ad serving event.""")
    user_longitude = models.FloatField(null=True, blank=True,
        help_text="""The longitude coordinate of the end-user associated with the ad serving event.""")
    user_continent = models.TextField(blank=True,
        help_text="""The continent of the end-user associated with the ad serving event.""")
    user_country = models.TextField(blank=True,
        help_text="""The country of the end-user associated with the ad serving event, as
derived from their IP address.""")
    user_state = models.TextField(blank=True,
        help_text="""The state or region of the end-user associated with the ad serving event,
as derived from their IP address.""")
    user_dma = models.TextField(blank=True,
        help_text="""(United States only) The DMA code of the end-user associated with the
ad serving event, as derived from their IP address.""")
    user_msa = models.TextField(blank=True,
        help_text="""The MSA code of the end-user associated with the ad serving event, as derived from their IP address.""")
    user_city = models.TextField(blank=True,
        help_text="""The city of the end-user associated with the ad serving event, as derived
from their IP address.""")
    user_zip = models.IntegerField(null=True, blank=True,
        help_text="""The ZIP code for the end-user associated with the ad serving event. For example: 90066""") 
    user_connection_speed = models.TextField(blank=True,
        help_text="""The Internet connection speed of the end-user's computing environment,
as derived from their IP address.""")
    user_connection_type = models.TextField(blank=True,
        help_text="""The connection type of the end-user's computing environment, as derived from their IP address. For example: Cable or Mobile Wireless""")
    user_device = models.TextField(blank=True,
        help_text="""The mobile device type of the end-user associated with the ad serving event. For example: Apple iPad or Motorola Droid""")
    mobile_carrier = models.TextField(blank=True,
        help_text="""The mobile carrier for the end-user's mobile device, using the Mobile Country Code (MCC) and Mobile Network Code (MNC); that is, MCC-MNC. For example: 310-410""")
    mobile_net_type = models.TextField(blank=True,
        help_text="""The mobile network connection type for the end-user associated with the ad serving event. For example: wifi""")
    user_screen_res = models.TextField(blank=True,
        help_text="""The screen resolution of the end-users computing environment.""")
    user_agent = models.TextField(blank=True,
        help_text="""The user agent string sent by the end-user's browser.""")
    browser_name = models.TextField(blank=True,
        help_text="""The short-form name of the end-user's browser""")
    browser_version = models.TextField(blank=True,
        help_text="""The version of the end-user's browser""")
    user_operating_system = models.TextField(blank=True,
        help_text="""m The operating system of the end-user's computing environment.""")
    user_os_version = models.TextField(blank=True,
        help_text="""The version of the end-user's operating system.""")
    browser_language = models.TextField(blank=True,
        help_text="""The language code sent by the end-user's browser. Most likely, this is the
preferred browsing language of the end-user.""")
    page_url = models.TextField(blank=True,
        help_text="""The URL of the webpage where the ad call originated.""")
    referrer_url = models.TextField(blank=True,
        help_text="""The URL of the referring webpage.""")  
    matched_targeting = models.TextField(blank=True,
        help_text="""This field is currently not used.""")
    custom_fields = models.TextField(blank=True,
        help_text="""A caret-delimited list of custom variables for the event. These are passed
as key-value pairs in the call, using the format: c.<key>=<value> For
example: c.gender=male or c.age=30.""")
    audience_segments = models.TextField(blank=True,
        help_text="""A comma-separated list of segment IDs to which the user was assigned at
the time of the request event.""")
    traffic_rejected = models.BooleanField(blank=True, default=False,
        help_text="""Summarizes traffic quality for the event 
(either True or False). For example, True indicates if any request, impression, or click was rejected based on traffic quality flags, such as IP blocklists.""")

    def __unicode__(self):
        return self.event_time

class ELFDataConversion(models.Model):
    event_time = models.DateTimeField(null=True, blank=True, 
        help_text="""The date and time of the actual conversion, using the format: 
YYYY-MM-DD hh:mm:ss. For example: 2011-02-28 12:45:30""")
    transaction_id = models.TextField(blank=True,
        help_text="""The unique ID for the original request event; OpenX generates this ID
for the request event, and includes this in feeds for subsequent related
events. For example: f0e6cd54-7232-4db5-8b25-c4ad7fdea840""")
    transaction_time = models.DateTimeField(null=True, blank=True, 
        help_text="""The date and time of the original request event, to which this ad serving
event is tied, using the format: YYYY-MM-DD hh:mm:ss. For example:
2011-02-28 12:45:30 (so, in the case of a request event, this time is
the same as the event_time).""")
    user_id = models.TextField(blank=True,
        help_text="""The unique ID for the user; OpenX generates this ID and tracks it
through request events. For example: 49be9663-ab0c-4af6-a1b1-
c9e357f523bd""")
    user_id_new = models.BooleanField(blank=True, default=False,
        help_text="""Indicates if OpenX generated the user ID on this request (True), or if it
originated in a separate request event (False).""")
    ad_unit_id = models.IntegerField(null=True, blank=True,
        help_text="""The unique ID of the ad unit associated with the conversion. For example:
3302""")
    ad_unit_grp_id = models.TextField(blank=True,
        help_text="""The unique ID of the ad unit group, if any, associated with the ad serving event. For example: 3492""")
    line_item_id  = models.IntegerField(null=True, blank=True,
        help_text="""The ID for the line item associated with the conversion. For example: 4389""")
    ad_id = models.IntegerField(null=True, blank=True,
        help_text="""The ID for the ad associated with the conversion. For example: 6732""")
    page_id  = models.IntegerField(null=True, blank=True,
        help_text="""The unique ID of the ad unit group, if any, associated with the conversion.
For example: 3492""")
    beacon_id = models.IntegerField(null=True, blank=True,
        help_text="""The ID for the beacon associated with the conversion. For example: 3344""")
    is_click = models.BooleanField(blank=True, default=False,
        help_text="""Indicates if the conversion was set by a click event (True) or an
impression event (False).""")
    ad_id = models.IntegerField(null=True, blank=True,
        help_text="""The ID for the ad associated with the conversion. For example: 6732""")
    action_type = models.TextField(null=True, blank=True,
        help_text="""The kind action that triggered the conversion beacon. For example:
sign-up or lead""")
    user_ip_address = models.TextField(blank=True,
        help_text="""The IP address of the end-user associated with the ad serving event.""")
    user_latitude = models.FloatField(null=True, blank=True,
        help_text="""The latitude coordinate of the end-user associated with the ad serving event.""")
    user_longitude = models.FloatField(null=True, blank=True,
        help_text="""The longitude coordinate of the end-user associated with the ad serving event.""")
    user_continent = models.TextField(blank=True,
        help_text="""The continent of the end-user associated with the ad serving event.""")
    user_country = models.TextField(blank=True,
        help_text="""The country of the end-user associated with the ad serving event, as
derived from their IP address.""")
    user_state = models.TextField(blank=True,
        help_text="""The state or region of the end-user associated with the ad serving event,
as derived from their IP address.""")
    user_dma = models.TextField(blank=True,
        help_text="""(United States only) The DMA code of the end-user associated with the
ad serving event, as derived from their IP address.""")
    user_msa = models.TextField(blank=True,
        help_text="""The MSA code of the end-user associated with the ad serving event, as derived from their IP address.""")
    user_city = models.TextField(blank=True,
        help_text="""The city of the end-user associated with the ad serving event, as derived
from their IP address.""")
    user_zip = models.IntegerField(null=True, blank=True,
        help_text="""""") 
    user_connection_speed = models.TextField(blank=True,
        help_text="""The Internet connection speed of the end-user's computing environment,
as derived from their IP address.""")
    user_connection_type = models.TextField(blank=True,
        help_text="""The connection type of the end-user's computing environment, as derived from their IP address. For example: Cable or Mobile Wireless""")
    user_agent = models.TextField(blank=True,
        help_text="""The user agent string sent by the end-user's browser.""")
    user_device = models.TextField(blank=True,
        help_text="""The mobile device type of the end-user associated with the ad serving event. For example: Apple iPad or Motorola Droid""")
    mobile_carrier = models.TextField(blank=True,
        help_text="""The mobile carrier for the end-user's mobile device, using the Mobile Country Code (MCC) and Mobile Network Code (MNC); that is, MCC-MNC. For example: 310-410""")
    mobile_net_type = models.TextField(blank=True,
        help_text="""The mobile network connection type for the end-user associated with the ad serving event. For example: wifi""")
    browser_name = models.TextField(blank=True,
        help_text="""The short-form name of the end-user's browser""")
    browser_version = models.TextField(blank=True,
        help_text="""The version of the end-user's browser""")
    user_operating_system = models.TextField(blank=True,
        help_text="""m The operating system of the end-user's computing environment.""")
    user_os_version = models.TextField(blank=True,
        help_text="""The version of the end-user's operating system.""")
    browser_language = models.TextField(blank=True,
        help_text="""The language code sent by the end-user's browser. Most likely, this is the
preferred browsing language of the end-user.""")
    page_url = models.TextField(blank=True,
        help_text="""The URL of the webpage where the ad call originated.""")
    referrer_url = models.TextField(blank=True,
        help_text="""The URL of the referring webpage.""")  
    custom_fields = models.TextField(blank=True,
        help_text="""A caret-delimited list of custom variables for the event. These are passed
as key-value pairs in the call, using the format: c.<key>=<value> For
example: c.gender=male or c.age=30.""")
    audience_segments = models.TextField(blank=True,
        help_text="""A comma-separated list of segment IDs to which the user was assigned at the time of the request event.""")
    traffic_rejected = models.BooleanField(blank=True, default=False,
        help_text="""Summarizes traffic quality for the event 
(either True or False). For example, True indicates if any request, impression, or click was rejected based on traffic quality flags, such as IP blocklists.""")

    def __unicode__(self):
        return self.event_time



####################
# OpenX data

class OpenXAccount(models.Model):
    primary_contact_id        = models.IntegerField(null=True)
    blocked_creativetypes     = models.TextField(null=True)
    ac_account_id             = models.IntegerField(null=True)
    total_impressions         = models.IntegerField(null=True)
    account_manager_id        = models.IntegerField(null=True)
    currency_id               = models.IntegerField(null=True)
    brands                    = models.TextField(null=True)
    filters                   = models.TextField(null=True)
    uplift                    = models.IntegerField(null=True)
    modified_date             = models.DateTimeField()
    sales_lead_id             = models.IntegerField(null=True)
    country_of_business_id    = models.TextField(null=True)
    blocked_contentattributes = models.TextField(null=True)
    blocked_languages         = models.TextField(null=True)
    clicks                    = models.IntegerField(null=True)
    allow_unbranded_buyers    = models.IntegerField(null=True)
    status                    = models.TextField(null=True)
    fill_rate                 = models.IntegerField(null=True)
    account_id                = models.IntegerField(null=True)
    exchange                  = models.TextField(null=True)
    deleted                   = models.IntegerField(null=True)
    buyer_breakout            = models.IntegerField(null=True)
    market_active             = models.IntegerField(null=True)
    single_ad_limitation      = models.IntegerField(null=True)
    account_type_id           = models.IntegerField(null=True)
    market_currency_id        = models.IntegerField(null=True)
    brand_labels              = models.TextField(null=True)
    name                      = models.TextField(null=True)
    timezone_id               = models.IntegerField(null=True)
    notes                     = models.TextField(null=True)
    total_conversions         = models.IntegerField(null=True)
    instance_id               = models.IntegerField(null=True)
    blocked_adcategories      = models.TextField(null=True)
    billing_contact_id        = models.IntegerField(null=True)
    created_date              = models.DateTimeField()
    domains                   = models.TextField(null=True)
    requests                  = models.IntegerField(null=True)
    external_id               = models.TextField(null=True)


class OpenXUser(models.Model):
    status                    = models.TextField(null=True)
    modified_date             = models.DateTimeField()
    first_name                = models.TextField(null=True)
    last_name                 = models.TextField(null=True)
    verified                  = models.IntegerField(null=True)
    account_id                = models.IntegerField(null=True)
    roles                     = models.TextField(null=True)
    locale                    = models.TextField(null=True)
    notes                     = models.TextField(null=True)
    deleted                   = models.IntegerField(null=True)
    default_report_range      = models.TextField(null=True)
    terms_accepted            = models.DateTimeField()
    created_date              = models.DateTimeField()
    external_id               = models.TextField(null=True)
    email                     = models.TextField(null=True)


class OpenXRole(models.Model):
    modified_date             = models.DateTimeField()
    name                      = models.TextField(null=True)
    deleted                   = models.IntegerField(null=True)
    acl_uid                   = models.TextField(null=True)
    system                    = models.IntegerField(null=True)
    compiled_acl              = models.TextField(null=True)
    created_date              = models.DateTimeField()
    account_id                = models.IntegerField(null=True)


class OpenXSite(models.Model):
    filters                   = models.TextField(null=True)
    domain_override           = models.TextField(null=True)
    blocked_creativetypes     = models.TextField(null=True)
    category_override         = models.IntegerField(null=True)
    modified_date             = models.DateTimeField()
    content_topic_id          = models.IntegerField(null=True)
    blocked_contentattributes = models.TextField(null=True)
    blocked_languages         = models.TextField(null=True)
    allow_unbranded_buyers    = models.IntegerField(null=True)
    status                    = models.TextField(null=True)
    account_id                = models.IntegerField(null=True)
    deleted                   = models.IntegerField(null=True)
    delivery_medium_id        = models.IntegerField(null=True)
    brands                    = models.TextField(null=True)
    name                      = models.TextField(null=True)
    brand_labels              = models.TextField(null=True)
    content_type_id           = models.IntegerField(null=True)
    url                       = models.TextField(null=True)
    notes                     = models.TextField(null=True)
    platform_id               = models.TextField(null=True)
    blocked_adcategories      = models.TextField(null=True)
    created_date              = models.DateTimeField()
    domains                   = models.TextField(null=True)
    external_id               = models.TextField(null=True)


class OpenXAdunit(models.Model):
    status                    = models.TextField(null=True)
    modified_date             = models.DateTimeField()
    sitesection_id            = models.IntegerField(null=True)
    name                      = models.TextField(null=True)
    content_type_id           = models.IntegerField(null=True)
    deleted                   = models.IntegerField(null=True)
    external_id               = models.TextField(null=True)
    site_id                   = models.IntegerField(null=True)
    alt_sizes                 = models.TextField(null=True)
    delivery_medium_id        = models.IntegerField(null=True)
    vast_tag                  = models.TextField(null=True)
    created_date              = models.DateTimeField()
    content_topics            = models.TextField(null=True)
    primary_size              = models.TextField(null=True)
    real_time_bid_floor       = models.DecimalField(max_digits=9, decimal_places=2)
    account_id                = models.IntegerField(null=True)


class OpenXAdunitgroup(models.Model):
    status                    = models.TextField(null=True)
    modified_date             = models.DateTimeField()
    adunits                   = models.TextField(null=True)
    name                      = models.TextField(null=True)
    deleted                   = models.IntegerField(null=True)
    description               = models.TextField(null=True)
    site_id                   = models.IntegerField(null=True)
    delivery_medium_id        = models.IntegerField(null=True)
    vast_tag                  = models.TextField(null=True)
    created_date              = models.DateTimeField()
    masteradunit_id           = models.IntegerField(null=True)
    external_id               = models.TextField(null=True)
    account_id                = models.IntegerField(null=True)


class OpenXOrder(models.Model):
    status                    = models.TextField(null=True)
    booking_account_id        = models.IntegerField(null=True)
    sales_lead_id             = models.IntegerField(null=True)
    primary_trafficker_id     = models.IntegerField(null=True)
    account_id                = models.IntegerField(null=True)
    end_date                  = models.DateTimeField()
    click_through_window      = models.IntegerField(null=True)
    deleted                   = models.IntegerField(null=True)
    notes                     = models.TextField(null=True)
    modified_date             = models.DateTimeField()
    budget                    = models.DecimalField(max_digits=11, decimal_places=2)
    secondary_trafficker_id   = models.IntegerField(null=True)
    primary_analyst_id        = models.IntegerField(null=True)
    creator_id                = models.IntegerField(null=True)
    single_ad_limitation      = models.IntegerField(null=True)
    created_date              = models.DateTimeField()
    view_through_window       = models.IntegerField(null=True)
    external_id               = models.TextField(null=True)
    start_date                = models.DateTimeField()
    name                      = models.TextField(null=True)


class OpenXLineitem(models.Model):
    pricing_model_id          = models.IntegerField(null=True)
    lifetime_impression_cap   = models.IntegerField(null=True)
    lifetime_click_cap        = models.IntegerField(null=True)
    companion_fill_method_id  = models.IntegerField(null=True)
    deliver_by_default        = models.IntegerField(null=True)
    daily_click_cap           = models.IntegerField(null=True)
    modified_date             = models.DateTimeField()
    make_good                 = models.IntegerField(null=True)
    ad_delivery_id            = models.IntegerField(null=True)
    share_of_voice            = models.DecimalField(max_digits=3, decimal_places=1)
    lifetime_action_cap       = models.IntegerField(null=True)
    pacing_model_id           = models.IntegerField(null=True)
    priority                  = models.IntegerField(null=True)
    deleted                   = models.IntegerField(null=True)
    buying_model_id           = models.IntegerField(null=True)
    daily_impression_goal     = models.BigIntegerField(null=True)
    start_date                = models.DateTimeField()
    status                    = models.TextField(null=True)
    session_duration          = models.IntegerField(null=True)
    account_id                = models.IntegerField(null=True)
    end_date                  = models.DateTimeField()
    order_id                  = models.IntegerField(null=True)
    targeting_rules           = models.TextField(null=True)
    session_display_cap       = models.IntegerField(null=True)
    delivery_medium_id        = models.IntegerField(null=True)
    individual_display_cap    = models.IntegerField(null=True)
    lifetime_impression_goal  = models.BigIntegerField(null=True)
    daily_impression_cap      = models.IntegerField(null=True)
    budget_type               = models.TextField(null=True)
    single_ad_limitation      = models.IntegerField(null=True)
    name                      = models.TextField(null=True)
    pricing_rate              = models.DecimalField(max_digits=11, decimal_places=4)
    oxtl                      = models.TextField(null=True)
    notes                     = models.TextField(null=True)
    created_date              = models.DateTimeField()
    external_id               = models.TextField(null=True)


class OpenXAd(models.Model):
    status                    = models.TextField(null=True)
    modified_date             = models.DateTimeField()
    days_of_week              = models.TextField(null=True)
    session_duration          = models.IntegerField(null=True)
    hours_of_day              = models.TextField(null=True)
    name                      = models.TextField(null=True)
    end_date                  = models.DateTimeField()
    deliver_by_default        = models.IntegerField(null=True)
    order_id                  = models.IntegerField(null=True)
    creative_id               = models.IntegerField(null=True)
    ad_weight                 = models.DecimalField(max_digits=3, decimal_places=1)
    deleted                   = models.IntegerField(null=True)
    session_display_cap       = models.IntegerField(null=True)
    ad_type_id                = models.IntegerField(null=True)
    individual_display_cap    = models.IntegerField(null=True)
    notes                     = models.TextField(null=True)
    lineitem_id               = models.IntegerField(null=True)
    created_date              = models.DateTimeField()
    external_id               = models.TextField(null=True)
    start_date                = models.DateTimeField()
    account_id                = models.IntegerField(null=True)


class OpenXCreative(models.Model):
    file2                     = models.TextField(null=True)
    account_id                = models.IntegerField(null=True)
    source                    = models.TextField(null=True)
    deleted                   = models.IntegerField(null=True)
    bitrate                   = models.DecimalField(max_digits=10, decimal_places=2)
    notes                     = models.TextField(null=True)
    created_date              = models.DateTimeField()
    modified_date             = models.DateTimeField()
    uri                       = models.TextField(null=True)
    height                    = models.IntegerField(null=True)
    ad_type_id                = models.IntegerField(null=True)
    width                     = models.IntegerField(null=True)
    orig_name                 = models.TextField(null=True)
    file                      = models.TextField(null=True)
    file_size                 = models.DecimalField(max_digits=11, decimal_places=2)
    duration                  = models.DecimalField(max_digits=10, decimal_places=2)
    external_id               = models.TextField(null=True)
    mime_type                 = models.TextField(null=True)
    name                      = models.TextField(null=True)


class OpenXRule(models.Model):
    modified_date             = models.DateTimeField()
    deleted                   = models.IntegerField(null=True)
    attribute                 = models.TextField(null=True)
    value                     = models.TextField(null=True)
    lineitem_id               = models.IntegerField(null=True)
    created_date              = models.DateTimeField()
    operator                  = models.TextField(null=True)
    external_id               = models.TextField(null=True)
    dimension                 = models.TextField(null=True)


class OpenXReport(models.Model):
    modified_date             = models.DateTimeField()
    user_id                   = models.IntegerField(null=True)
    name                      = models.TextField(null=True)
    deleted                   = models.IntegerField(null=True)
    parameter_string          = models.TextField(null=True)
    created_date              = models.DateTimeField()
    relative_date             = models.TextField(null=True)