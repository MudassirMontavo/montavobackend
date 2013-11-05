import re
from django.db import models
from spendata.signals import post_save_add_user_id

ACXIOM_FIELD_MAPPING = {
    'DisplayName'      : 'display_name',
    'BusinessName'     : 'business_name',
    'Corporate Name'   : 'corporate_name',
    'StreetNumber'     : 'street_number',
    'StreetDirectional': 'street_directional',
    'StreetName'       : 'street_name',
    'StreetSuffix'     : 'street_suffix',
    'PostDirectional'  : 'post_directional',
    'UnitDesignator'   : 'unit_designator',
    'UnitNumber'       : 'unit_number',
    'CityName'         : 'city_name',
    'StateCode'        : 'state_code',
    'Zip'              : 'zip_code',
    'Latitude'         : 'latitude',
    'Longitude'        : 'longitude',
}


class AcxiomData(models.Model):
    display_name       = models.TextField(blank=True)
    business_name      = models.TextField(blank=True)
    corporate_name     = models.TextField(blank=True)
    street_number      = models.TextField(blank=True)
    street_directional = models.TextField(blank=True)
    street_name        = models.TextField(blank=True)
    street_suffix      = models.TextField(blank=True)
    post_directional   = models.TextField(blank=True)
    unit_designator    = models.TextField(blank=True)
    unit_number        = models.TextField(blank=True)
    city_name          = models.TextField(blank=True)
    state_code         = models.TextField(blank=True)
    zip_code           = models.TextField(null=True)
    latitude           = models.FloatField(null=True, blank=True)
    longitude          = models.FloatField(null=True, blank=True)

    def __unicode__(self):
        return self.business_name


class MobileAppUserData(models.Model):
    user_id       = models.TextField(blank=True, unique=True, db_index=True)
    first_name    = models.TextField(blank=True)
    last_name     = models.TextField(blank=True)
    mobile_number = models.TextField(blank=True)
    gender        = models.TextField(blank=True)
    user_city     = models.TextField(blank=True)
    user_state    = models.TextField(blank=True)
    user_zip      = models.IntegerField(null=True, blank=True)
    user_country  = models.TextField(blank=True)
    user_email    = models.TextField(blank=True, db_index=True)
    income_range  = models.TextField(blank=True)
    age_range     = models.TextField(blank=True)
    area_code     = models.TextField(blank=True)

    def __unicode__(self):
        return str(self.user_id)


class MobileAppMobileData(models.Model):
    device_id           = models.TextField(blank=True, unique=True, db_index=True)
    user_id             = models.TextField(blank=True, db_index=True)
    wireless_carrier    = models.TextField(blank=True)
    device_manufacturer = models.TextField(blank=True)
    device_model        = models.TextField(blank=True)

    def _get_user(self):
        try:
            return MobileAppUserData.objects.get(user_id=self.user_id)
        except MobileAppMobileData.DoesNotExist:
            return None

    mobile_user = property(_get_user)

    def __unicode__(self):
        return str(self.device_id)


class MobileAppLocationData(models.Model):
    device_id        = models.TextField(blank=True, db_index=True)
    user_latitude    = models.FloatField(null=True, blank=True)
    user_longitude   = models.FloatField(null=True, blank=True)
    capture_time_utc = models.DateTimeField(null=True, blank=True)

    def _get_device(self):
        try:
            return MobileAppMobileData.objects.get(device_id=self.device_id)
        except MobileAppMobileData.DoesNotExist:
            return None

    mobile_device = property(_get_device)

    def __unicode__(self):
        return str(self.capture_time_utc)


class MobileAppUserHomeCircle(models.Model):
    user_id   = models.TextField(blank=True, db_index=True)
    latitude  = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    weighting = models.FloatField(null=True, blank=True)
    updated   = models.DateTimeField(editable=False, auto_now=True)

    def _get_user(self):
        try:
            return MobileAppUserData.objects.get(user_id=self.user_id)
        except MobileAppUserData.DoesNotExist:
            return None

    mobile_user = property(_get_user)


class ELFCommonData(models.Model):

    """ Abstract base class for Request"""
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
    advertiser_id = models.IntegerField(null=True, blank=True, db_index=True,
        help_text="""The ID for the advertiser account whose ad serves to the ad inventory
associated with the ad serving event. For example: 56309""")
    order_id = models.IntegerField(null=True, blank=True,
        help_text="""The ID for the order associated with the ad serving event. For example:
876""")
    line_item_id = models.IntegerField(null=True, blank=True,
        help_text="""The ID for the line item associated with the ad serving event. For
example: 4389""")
    ad_id = models.IntegerField(null=True, blank=True, db_index=True,
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
    serial_number = models.IntegerField(null=True, blank=True) 
    part_id = models.IntegerField(null=True, blank=True)
    revision = models.IntegerField(default=1)
    user_id = models.TextField(blank=True, db_index=True)

    def _get_device(self):
        r = re.findall(r"deviceid\=([^^]+)", self.custom_fields)
        if not r:
            return None
        device_id = r[0]
        try:
            return MobileAppMobileData.objects.get(device_id=device_id)
        except MobileAppMobileData.DoesNotExist:
            return None

    mobile_device = property(_get_device)

    def __unicode__(self):
        return str(self.event_time)

    class Meta:
        abstract = True


class ELFRequestData(ELFCommonData):
    pass


class ELFImpressionData(ELFCommonData):
    pass


class ELFClickData(ELFCommonData):
    pass


class ELFRequestSerial(models.Model):
    serial_number = models.IntegerField(null=True, blank=True)


class ELFImpressionSerial(models.Model):
    serial_number = models.IntegerField(null=True, blank=True)


class ELFClickSerial(models.Model):
    serial_number = models.IntegerField(null=True, blank=True)


class ELFConversionSerial(models.Model):
    serial_number = models.IntegerField(null=True, blank=True)


class ELFConversionData(models.Model):
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
    ad_id = models.IntegerField(null=True, blank=True, db_index=True,
        help_text="""The ID for the ad associated with the conversion. For example: 6732""")
    page_id  = models.IntegerField(null=True, blank=True,
        help_text="""The unique ID of the ad unit group, if any, associated with the conversion.
For example: 3492""")
    beacon_id = models.IntegerField(null=True, blank=True,
        help_text="""The ID for the beacon associated with the conversion. For example: 3344""")
    is_click = models.BooleanField(blank=True, default=False,
        help_text="""Indicates if the conversion was set by a click event (True) or an
impression event (False).""")
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
    user_id = models.TextField(blank=True, db_index=True)

    def _get_device(self):
        r = re.findall(r"deviceid\=([^^]+)", self.custom_fields)
        if not r:
            return None
        device_id = r[0]
        try:
            return MobileAppMobileData.objects.get(device_id=device_id)
        except MobileAppMobileData.DoesNotExist:
            return None

    mobile_device = property(_get_device)

    def __unicode__(self):
        return str(self.event_time)

# Signal connections
for model in (ELFRequestData, ELFImpressionData, ELFClickData, ELFConversionData):
    models.signals.post_save.connect(
        post_save_add_user_id,
        sender=model,
        dispatch_uid='spendata.post_save_%s' % model,
    )

####################
# OpenX data


class OpenXAccount(models.Model):
    primary_contact_id        = models.IntegerField(null=True, blank=True)
    blocked_creativetypes     = models.TextField(blank=True)
    ac_account_id             = models.IntegerField(null=True, blank=True)
    total_impressions         = models.IntegerField(null=True, blank=True)
    account_manager_id        = models.IntegerField(null=True, blank=True)
    currency_id               = models.IntegerField(null=True, blank=True)
    brands                    = models.TextField(blank=True)
    filters                   = models.TextField(blank=True)
    uplift                    = models.IntegerField(null=True, blank=True)
    modified_date             = models.DateTimeField(null=True, blank=True)
    sales_lead_id             = models.IntegerField(null=True, blank=True)
    country_of_business_id    = models.TextField(blank=True)
    blocked_contentattributes = models.TextField(blank=True)
    blocked_languages         = models.TextField(blank=True)
    clicks                    = models.IntegerField(null=True, blank=True)
    allow_unbranded_buyers    = models.IntegerField(null=True, blank=True)
    status                    = models.TextField(blank=True)
    fill_rate                 = models.IntegerField(null=True, blank=True)
    account_id                = models.IntegerField(null=True, blank=True)
    exchange                  = models.TextField(blank=True)
    deleted                   = models.IntegerField(null=True, blank=True)
    buyer_breakout            = models.IntegerField(null=True, blank=True)
    market_active             = models.IntegerField(null=True, blank=True)
    single_ad_limitation      = models.IntegerField(null=True, blank=True)
    account_type_id           = models.IntegerField(null=True, blank=True)
    market_currency_id        = models.IntegerField(null=True, blank=True)
    brand_labels              = models.TextField(blank=True)
    name                      = models.TextField(blank=True)
    timezone_id               = models.IntegerField(null=True, blank=True)
    notes                     = models.TextField(blank=True)
    total_conversions         = models.IntegerField(null=True, blank=True)
    instance_id               = models.IntegerField(null=True, blank=True)
    blocked_adcategories      = models.TextField(blank=True)
    billing_contact_id        = models.IntegerField(null=True, blank=True)
    created_date              = models.DateTimeField(null=True, blank=True)
    domains                   = models.TextField(blank=True)
    requests                  = models.IntegerField(null=True, blank=True)
    external_id               = models.TextField(blank=True)


class OpenXUser(models.Model):
    status                    = models.TextField(blank=True)
    modified_date             = models.DateTimeField(null=True, blank=True)
    first_name                = models.TextField(blank=True)
    last_name                 = models.TextField(blank=True)
    verified                  = models.IntegerField(null=True, blank=True)
    account_id                = models.IntegerField(null=True, blank=True)
    roles                     = models.TextField(blank=True)
    locale                    = models.TextField(blank=True)
    notes                     = models.TextField(blank=True)
    deleted                   = models.IntegerField(null=True, blank=True)
    default_report_range      = models.TextField(blank=True)
    terms_accepted            = models.DateTimeField(null=True, blank=True)
    created_date              = models.DateTimeField(null=True, blank=True)
    external_id               = models.TextField(blank=True)
    email                     = models.TextField(blank=True)


class OpenXRole(models.Model):
    modified_date             = models.DateTimeField(null=True, blank=True)
    name                      = models.TextField(blank=True)
    deleted                   = models.IntegerField(null=True, blank=True)
    acl_uid                   = models.TextField(blank=True)
    system                    = models.IntegerField(null=True, blank=True)
    compiled_acl              = models.TextField(blank=True)
    created_date              = models.DateTimeField(null=True, blank=True)
    account_id                = models.IntegerField(null=True, blank=True)


class OpenXSite(models.Model):
    filters                   = models.TextField(blank=True)
    domain_override           = models.TextField(blank=True)
    blocked_creativetypes     = models.TextField(blank=True)
    category_override         = models.IntegerField(null=True, blank=True)
    modified_date             = models.DateTimeField(null=True, blank=True)
    content_topic_id          = models.IntegerField(null=True, blank=True)
    blocked_contentattributes = models.TextField(blank=True)
    blocked_languages         = models.TextField(blank=True)
    allow_unbranded_buyers    = models.IntegerField(null=True, blank=True)
    status                    = models.TextField(blank=True)
    account_id                = models.IntegerField(null=True, blank=True)
    deleted                   = models.IntegerField(null=True, blank=True)
    delivery_medium_id        = models.IntegerField(null=True, blank=True)
    brands                    = models.TextField(blank=True)
    name                      = models.TextField(blank=True)
    brand_labels              = models.TextField(blank=True)
    content_type_id           = models.IntegerField(null=True, blank=True)
    url                       = models.TextField(blank=True)
    notes                     = models.TextField(blank=True)
    platform_id               = models.TextField(blank=True)
    blocked_adcategories      = models.TextField(blank=True)
    created_date              = models.DateTimeField(null=True, blank=True)
    domains                   = models.TextField(blank=True)
    external_id               = models.TextField(blank=True)


class OpenXAdunit(models.Model):
    status                    = models.TextField(blank=True)
    modified_date             = models.DateTimeField(null=True, blank=True)
    sitesection_id            = models.IntegerField(null=True, blank=True)
    name                      = models.TextField(blank=True)
    content_type_id           = models.IntegerField(null=True, blank=True)
    deleted                   = models.IntegerField(null=True, blank=True)
    external_id               = models.TextField(blank=True)
    site_id                   = models.IntegerField(null=True, blank=True)
    alt_sizes                 = models.TextField(blank=True)
    delivery_medium_id        = models.IntegerField(null=True, blank=True)
    vast_tag                  = models.TextField(blank=True)
    created_date              = models.DateTimeField(null=True, blank=True)
    content_topics            = models.TextField(blank=True)
    primary_size              = models.TextField(blank=True)
    real_time_bid_floor       = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    account_id                = models.IntegerField(null=True, blank=True)


class OpenXAdunitgroup(models.Model):
    status                    = models.TextField(blank=True)
    modified_date             = models.DateTimeField(null=True, blank=True)
    adunits                   = models.TextField(blank=True)
    name                      = models.TextField(blank=True)
    deleted                   = models.IntegerField(null=True, blank=True)
    description               = models.TextField(blank=True)
    site_id                   = models.IntegerField(null=True, blank=True)
    delivery_medium_id        = models.IntegerField(null=True, blank=True)
    vast_tag                  = models.TextField(blank=True)
    created_date              = models.DateTimeField(null=True, blank=True)
    masteradunit_id           = models.IntegerField(null=True, blank=True)
    external_id               = models.TextField(blank=True)
    account_id                = models.IntegerField(null=True, blank=True)


class OpenXOrder(models.Model):
    status                    = models.TextField(blank=True)
    booking_account_id        = models.IntegerField(null=True, blank=True)
    sales_lead_id             = models.IntegerField(null=True, blank=True)
    primary_trafficker_id     = models.IntegerField(null=True, blank=True)
    account_id                = models.IntegerField(null=True, blank=True)
    end_date                  = models.DateTimeField(null=True, blank=True)
    click_through_window      = models.IntegerField(null=True, blank=True)
    deleted                   = models.IntegerField(null=True, blank=True)
    notes                     = models.TextField(blank=True)
    modified_date             = models.DateTimeField(null=True, blank=True)
    budget                    = models.DecimalField(max_digits=11, decimal_places=2, null=True, blank=True)
    secondary_trafficker_id   = models.IntegerField(null=True, blank=True)
    primary_analyst_id        = models.IntegerField(null=True, blank=True)
    creator_id                = models.IntegerField(null=True, blank=True)
    single_ad_limitation      = models.IntegerField(null=True, blank=True)
    created_date              = models.DateTimeField(null=True, blank=True)
    view_through_window       = models.IntegerField(null=True, blank=True)
    external_id               = models.TextField(blank=True)
    start_date                = models.DateTimeField(null=True, blank=True)
    name                      = models.TextField(blank=True)


class OpenXLineitem(models.Model):
    pricing_model_id          = models.IntegerField(null=True, blank=True)
    lifetime_impression_cap   = models.IntegerField(null=True, blank=True)
    lifetime_click_cap        = models.IntegerField(null=True, blank=True)
    companion_fill_method_id  = models.IntegerField(null=True, blank=True)
    deliver_by_default        = models.IntegerField(null=True, blank=True)
    daily_click_cap           = models.IntegerField(null=True, blank=True)
    modified_date             = models.DateTimeField(null=True, blank=True)
    make_good                 = models.IntegerField(null=True, blank=True)
    ad_delivery_id            = models.IntegerField(null=True, blank=True)
    share_of_voice            = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    lifetime_action_cap       = models.IntegerField(null=True, blank=True)
    pacing_model_id           = models.IntegerField(null=True, blank=True)
    priority                  = models.IntegerField(null=True, blank=True)
    deleted                   = models.IntegerField(null=True, blank=True)
    buying_model_id           = models.IntegerField(null=True, blank=True)
    daily_impression_goal     = models.BigIntegerField(null=True, blank=True)
    start_date                = models.DateTimeField(null=True, blank=True)
    status                    = models.TextField(blank=True)
    session_duration          = models.IntegerField(null=True, blank=True)
    account_id                = models.IntegerField(null=True, blank=True)
    end_date                  = models.DateTimeField(null=True, blank=True)
    order_id                  = models.IntegerField(null=True, blank=True)
    targeting_rules           = models.TextField(blank=True)
    session_display_cap       = models.IntegerField(null=True, blank=True)
    delivery_medium_id        = models.IntegerField(null=True, blank=True)
    individual_display_cap    = models.IntegerField(null=True, blank=True)
    lifetime_impression_goal  = models.BigIntegerField(null=True, blank=True)
    daily_impression_cap      = models.IntegerField(null=True, blank=True)
    budget_type               = models.TextField(blank=True)
    single_ad_limitation      = models.IntegerField(null=True, blank=True)
    name                      = models.TextField(blank=True)
    pricing_rate              = models.DecimalField(max_digits=11, decimal_places=4, null=True, blank=True)
    oxtl                      = models.TextField(blank=True)
    notes                     = models.TextField(blank=True)
    created_date              = models.DateTimeField(null=True, blank=True)
    external_id               = models.TextField(blank=True)


class OpenXAd(models.Model):
    status                    = models.TextField(blank=True)
    modified_date             = models.DateTimeField(null=True, blank=True)
    days_of_week              = models.TextField(blank=True)
    session_duration          = models.IntegerField(null=True, blank=True)
    hours_of_day              = models.TextField(blank=True)
    name                      = models.TextField(blank=True)
    end_date                  = models.DateTimeField(null=True, blank=True)
    deliver_by_default        = models.IntegerField(null=True, blank=True)
    order_id                  = models.IntegerField(null=True, blank=True)
    creative_id               = models.IntegerField(null=True, blank=True)
    ad_weight                 = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    deleted                   = models.IntegerField(null=True, blank=True)
    session_display_cap       = models.IntegerField(null=True, blank=True)
    ad_type_id                = models.IntegerField(null=True, blank=True)
    individual_display_cap    = models.IntegerField(null=True, blank=True)
    notes                     = models.TextField(blank=True)
    lineitem_id               = models.IntegerField(null=True, blank=True)
    created_date              = models.DateTimeField(null=True, blank=True)
    external_id               = models.TextField(blank=True)
    start_date                = models.DateTimeField(null=True, blank=True)
    account_id                = models.IntegerField(null=True, blank=True)


class OpenXCreative(models.Model):
    file2                     = models.TextField(blank=True)
    account_id                = models.IntegerField(null=True, blank=True)
    source                    = models.TextField(blank=True)
    deleted                   = models.IntegerField(null=True, blank=True)
    bitrate                   = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    notes                     = models.TextField(blank=True)
    created_date              = models.DateTimeField(null=True, blank=True)
    modified_date             = models.DateTimeField(null=True, blank=True)
    uri                       = models.TextField(blank=True)
    height                    = models.IntegerField(null=True, blank=True)
    ad_type_id                = models.IntegerField(null=True, blank=True)
    width                     = models.IntegerField(null=True, blank=True)
    orig_name                 = models.TextField(blank=True)
    file                      = models.TextField(blank=True)
    file_size                 = models.DecimalField(max_digits=11, decimal_places=2, null=True, blank=True)
    duration                  = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    external_id               = models.TextField(blank=True)
    mime_type                 = models.TextField(blank=True)
    name                      = models.TextField(blank=True)


class OpenXRule(models.Model):
    modified_date             = models.DateTimeField(null=True, blank=True)
    deleted                   = models.IntegerField(null=True, blank=True)
    attribute                 = models.TextField(blank=True)
    value                     = models.TextField(blank=True)
    lineitem_id               = models.IntegerField(null=True, blank=True)
    created_date              = models.DateTimeField(null=True, blank=True)
    operator                  = models.TextField(blank=True)
    external_id               = models.TextField(blank=True)
    dimension                 = models.TextField(blank=True)


class OpenXReport(models.Model):
    modified_date             = models.DateTimeField(null=True, blank=True)
    user_id                   = models.IntegerField(null=True, blank=True)
    name                      = models.TextField(blank=True)
    deleted                   = models.IntegerField(null=True, blank=True)
    parameter_string          = models.TextField(blank=True)
    created_date              = models.DateTimeField(null=True, blank=True)
    relative_date             = models.TextField(blank=True)

#################
# Acxiom Data
class AcxiomBdfGroups(models.Model):
    recordid                  = models.TextField(blank=True)
    businessname              = models.TextField(blank=True)
    fulladdress               = models.TextField(blank=True)
    streetnumber              = models.TextField(blank=True)
    streetdirectional         = models.TextField(blank=True)
    streetname                = models.TextField(blank=True)
    streetsuffix              = models.TextField(blank=True)
    postdirectional           = models.TextField(blank=True)
    unitdesignator            = models.TextField(blank=True)
    unitnumber                = models.TextField(blank=True)
    cityname                  = models.TextField(blank=True)
    statecode                 = models.TextField(blank=True)
    zipcode                   = models.TextField(blank=True)
    zip4                      = models.TextField(blank=True)
    addresstypeindicator      = models.TextField(blank=True)
    deliverabilityindicator   = models.TextField(blank=True)
    phone                     = models.TextField(blank=True)
    phonecode                 = models.TextField(blank=True)
    pubdate                   = models.TextField(blank=True)
    solicitationrestrictions  = models.TextField(blank=True)
    primarybusinessclassificationflag = models.TextField(blank=True)
    sic1                      = models.TextField(blank=True)
    sic2                      = models.TextField(blank=True)
    sic3                      = models.TextField(blank=True)
    sic4                      = models.TextField(blank=True)
    sic5                      = models.TextField(blank=True)
    sic6                      = models.TextField(blank=True)
    businessflag              = models.TextField(blank=True)
    filemaintenanceflag       = models.TextField(blank=True)
    latitude                  = models.TextField(blank=True)
    longitude                 = models.TextField(blank=True)
    precisioncode             = models.TextField(blank=True)
    fips                      = models.TextField(blank=True)
    rbocunique                = models.TextField(blank=True)
    vanitycityname            = models.TextField(blank=True)
    booknumber                = models.TextField(blank=True)
    directorypage             = models.TextField(blank=True)
    recordnumber              = models.TextField(blank=True)
    webaddress                = models.TextField(blank=True)
    bdc1                      = models.TextField(blank=True)
    bdc2                      = models.TextField(blank=True)
    bdc3                      = models.TextField(blank=True)
    bdc4                      = models.TextField(blank=True)
    bdc5                      = models.TextField(blank=True)
    bdc6                      = models.TextField(blank=True)
    captioncounter            = models.TextField(blank=True)
    caption1                  = models.TextField(blank=True)
    caption2                  = models.TextField(blank=True)
    caption3                  = models.TextField(blank=True)
    caption4                  = models.TextField(blank=True)
    caption5                  = models.TextField(blank=True)
    caption6                  = models.TextField(blank=True)
    msa                       = models.TextField(blank=True)
    naics1                    = models.TextField(blank=True)
    naics2                    = models.TextField(blank=True)
    naics3                    = models.TextField(blank=True)
    naics4                    = models.TextField(blank=True)
    naics5                    = models.TextField(blank=True)
    naics6                    = models.TextField(blank=True)
    fax                       = models.TextField(blank=True)
    captionparentflag         = models.TextField(blank=True)
    captionsequencenumber     = models.TextField(blank=True)
    sectionnumber             = models.TextField(blank=True)
    changecode                = models.TextField(blank=True)
    verificationflag          = models.TextField(blank=True)
    bcsflag                   = models.TextField(blank=True)
    syph1                     = models.TextField(blank=True)
    syph2                     = models.TextField(blank=True)
    syph3                     = models.TextField(blank=True)
    syph4                     = models.TextField(blank=True)
    syph5                     = models.TextField(blank=True)
    syph6                     = models.TextField(blank=True)
    transactioncreatedate     = models.TextField(blank=True)
    salesvolume               = models.TextField(blank=True)
    employeesize              = models.TextField(blank=True)
    contactfirstname          = models.TextField(blank=True)
    contactlastname           = models.TextField(blank=True)
    contacttitle              = models.TextField(blank=True)
    contactgender             = models.TextField(blank=True)
    sohoflag                  = models.TextField(blank=True)
    ethnicownedbusiness       = models.TextField(blank=True)
    womenownedbusiness        = models.TextField(blank=True)
    masterrecordid            = models.TextField(blank=True)
    secondphonenumber         = models.TextField(blank=True)
    secondphonenumbercode     = models.TextField(blank=True)
    ageofrecord               = models.TextField(blank=True)
    addressprivacyflag        = models.TextField(blank=True)
    chainid                   = models.TextField(blank=True)
    cbsa                      = models.TextField(blank=True)


class AcxiomBdfIndex(models.Model):
    recordid                  = models.TextField(blank=True)
    oneperid                  = models.TextField(blank=True)
    oneperflag                = models.TextField(blank=True)
    orgflag                   = models.TextField(blank=True)
    groupflag                 = models.TextField(blank=True)
    ebdfflag                  = models.TextField(blank=True)
    masterrecordid            = models.TextField(blank=True)


class AcxiomBdfOrgs(models.Model):
    recordid                  = models.TextField(blank=True)
    businessname              = models.TextField(blank=True)
    fulladdress               = models.TextField(blank=True)
    streetnumber              = models.TextField(blank=True)
    streetdirectional         = models.TextField(blank=True)
    streetname                = models.TextField(blank=True)
    streetsuffix              = models.TextField(blank=True)
    postdirectional           = models.TextField(blank=True)
    unitdesignator            = models.TextField(blank=True)
    unitnumber                = models.TextField(blank=True)
    cityname                  = models.TextField(blank=True)
    statecode                 = models.TextField(blank=True)
    zipcode                   = models.TextField(blank=True)
    zip4                      = models.TextField(blank=True)
    addresstypeindicator      = models.TextField(blank=True)
    deliverabilityindicator   = models.TextField(blank=True)
    phone                     = models.TextField(blank=True)
    phonecode                 = models.TextField(blank=True)
    pubdate                   = models.TextField(blank=True)
    solicitationrestrictions  = models.TextField(blank=True)
    primarybusinessclassificationflag = models.TextField(blank=True)
    sic1                      = models.TextField(blank=True)
    sic2                      = models.TextField(blank=True)
    sic3                      = models.TextField(blank=True)
    sic4                      = models.TextField(blank=True)
    sic5                      = models.TextField(blank=True)
    sic6                      = models.TextField(blank=True)
    businessflag              = models.TextField(blank=True)
    filemaintenanceflag       = models.TextField(blank=True)
    latitude                  = models.TextField(blank=True)
    longitude                 = models.TextField(blank=True)
    precisioncode             = models.TextField(blank=True)
    fips                      = models.TextField(blank=True)
    rbocunique                = models.TextField(blank=True)
    vanitycityname            = models.TextField(blank=True)
    booknumber                = models.TextField(blank=True)
    directorypage             = models.TextField(blank=True)
    recordnumber              = models.TextField(blank=True)
    webaddress                = models.TextField(blank=True)
    bdc1                      = models.TextField(blank=True)
    bdc2                      = models.TextField(blank=True)
    bdc3                      = models.TextField(blank=True)
    bdc4                      = models.TextField(blank=True)
    bdc5                      = models.TextField(blank=True)
    bdc6                      = models.TextField(blank=True)
    captioncounter            = models.TextField(blank=True)
    caption1                  = models.TextField(blank=True)
    caption2                  = models.TextField(blank=True)
    caption3                  = models.TextField(blank=True)
    caption4                  = models.TextField(blank=True)
    caption5                  = models.TextField(blank=True)
    caption6                  = models.TextField(blank=True)
    msa                       = models.TextField(blank=True)
    naics1                    = models.TextField(blank=True)
    naics2                    = models.TextField(blank=True)
    naics3                    = models.TextField(blank=True)
    naics4                    = models.TextField(blank=True)
    naics5                    = models.TextField(blank=True)
    naics6                    = models.TextField(blank=True)
    fax                       = models.TextField(blank=True)
    captionparentflag         = models.TextField(blank=True)
    captionsequencenumber     = models.TextField(blank=True)
    sectionnumber             = models.TextField(blank=True)
    changecode                = models.TextField(blank=True)
    verificationflag          = models.TextField(blank=True)
    bcsflag                   = models.TextField(blank=True)
    syph1                     = models.TextField(blank=True)
    syph2                     = models.TextField(blank=True)
    syph3                     = models.TextField(blank=True)
    syph4                     = models.TextField(blank=True)
    syph5                     = models.TextField(blank=True)
    syph6                     = models.TextField(blank=True)
    transactioncreatedate     = models.TextField(blank=True)
    salesvolume               = models.TextField(blank=True)
    employeesize              = models.TextField(blank=True)
    contactfirstname          = models.TextField(blank=True)
    contactlastname           = models.TextField(blank=True)
    contacttitle              = models.TextField(blank=True)
    contactgender             = models.TextField(blank=True)
    sohoflag                  = models.TextField(blank=True)
    ethnicownedbusiness       = models.TextField(blank=True)
    womenownedbusiness        = models.TextField(blank=True)
    masterrecordid            = models.TextField(blank=True)
    secondphonenumber         = models.TextField(blank=True)
    secondphonenumbercode     = models.TextField(blank=True)
    ageofrecord               = models.TextField(blank=True)
    addressprivacyflag        = models.TextField(blank=True)
    chainid                   = models.TextField(blank=True)
    cbsa                      = models.TextField(blank=True)


class AcxiomBdfPrimary(models.Model):
    recordid                  = models.TextField(blank=True)
    businessname              = models.TextField(blank=True)
    fulladdress               = models.TextField(blank=True)
    streetnumber              = models.TextField(blank=True)
    streetdirectional         = models.TextField(blank=True)
    streetname                = models.TextField(blank=True)
    streetsuffix              = models.TextField(blank=True)
    postdirectional           = models.TextField(blank=True)
    unitdesignator            = models.TextField(blank=True)
    unitnumber                = models.TextField(blank=True)
    cityname                  = models.TextField(blank=True)
    statecode                 = models.TextField(blank=True)
    zipcode                   = models.TextField(blank=True)
    zip4                      = models.TextField(blank=True)
    addresstypeindicator      = models.TextField(blank=True)
    deliverabilityindicator   = models.TextField(blank=True)
    phone                     = models.TextField(blank=True)
    phonecode                 = models.TextField(blank=True)
    pubdate                   = models.TextField(blank=True)
    solicitationrestrictions  = models.TextField(blank=True)
    primarybusinessclassificationflag = models.TextField(blank=True)
    sic1                      = models.TextField(blank=True)
    sic2                      = models.TextField(blank=True)
    sic3                      = models.TextField(blank=True)
    sic4                      = models.TextField(blank=True)
    sic5                      = models.TextField(blank=True)
    sic6                      = models.TextField(blank=True)
    businessflag              = models.TextField(blank=True)
    filemaintenanceflag       = models.TextField(blank=True)
    latitude                  = models.TextField(blank=True)
    longitude                 = models.TextField(blank=True)
    precisioncode             = models.TextField(blank=True)
    fips                      = models.TextField(blank=True)
    rbocunique                = models.TextField(blank=True)
    vanitycityname            = models.TextField(blank=True)
    booknumber                = models.TextField(blank=True)
    directorypage             = models.TextField(blank=True)
    recordnumber              = models.TextField(blank=True)
    webaddress                = models.TextField(blank=True)
    bdc1                      = models.TextField(blank=True)
    bdc2                      = models.TextField(blank=True)
    bdc3                      = models.TextField(blank=True)
    bdc4                      = models.TextField(blank=True)
    bdc5                      = models.TextField(blank=True)
    bdc6                      = models.TextField(blank=True)
    captioncounter            = models.TextField(blank=True)
    caption1                  = models.TextField(blank=True)
    caption2                  = models.TextField(blank=True)
    caption3                  = models.TextField(blank=True)
    caption4                  = models.TextField(blank=True)
    caption5                  = models.TextField(blank=True)
    caption6                  = models.TextField(blank=True)
    msa                       = models.TextField(blank=True)
    naics1                    = models.TextField(blank=True)
    naics2                    = models.TextField(blank=True)
    naics3                    = models.TextField(blank=True)
    naics4                    = models.TextField(blank=True)
    naics5                    = models.TextField(blank=True)
    naics6                    = models.TextField(blank=True)
    fax                       = models.TextField(blank=True)
    captionparentflag         = models.TextField(blank=True)
    captionsequencenumber     = models.TextField(blank=True)
    sectionnumber             = models.TextField(blank=True)
    changecode                = models.TextField(blank=True)
    verificationflag          = models.TextField(blank=True)
    bcsflag                   = models.TextField(blank=True)
    syph1                     = models.TextField(blank=True)
    syph2                     = models.TextField(blank=True)
    syph3                     = models.TextField(blank=True)
    syph4                     = models.TextField(blank=True)
    syph5                     = models.TextField(blank=True)
    syph6                     = models.TextField(blank=True)
    transactioncreatedate     = models.TextField(blank=True)
    salesvolume               = models.TextField(blank=True)
    employeesize              = models.TextField(blank=True)
    contactfirstname          = models.TextField(blank=True)
    contactlastname           = models.TextField(blank=True)
    contacttitle              = models.TextField(blank=True)
    contactgender             = models.TextField(blank=True)
    sohoflag                  = models.TextField(blank=True)
    ethnicownedbusiness       = models.TextField(blank=True)
    womenownedbusiness        = models.TextField(blank=True)
    masterrecordid            = models.TextField(blank=True)
    secondphonenumber         = models.TextField(blank=True)
    secondphonenumbercode     = models.TextField(blank=True)
    ageofrecord               = models.TextField(blank=True)
    addressprivacyflag        = models.TextField(blank=True)
    chainid                   = models.TextField(blank=True)
    cbsa                      = models.TextField(blank=True)


class AcxiomEbdfOrd(models.Model):
    masterrecordid            = models.TextField(blank=True)
    recordid                  = models.TextField(blank=True)
    directorynumber           = models.TextField(blank=True)
    pubdate                   = models.TextField(blank=True)
    displayname               = models.TextField(blank=True)
    businessname              = models.TextField(blank=True)
    corporatename             = models.TextField(blank=True)
    streetnumber              = models.TextField(blank=True)
    streetdirectional         = models.TextField(blank=True)
    streetname                = models.TextField(blank=True)
    streetsuffix              = models.TextField(blank=True)
    postdirectional           = models.TextField(blank=True)
    unitdesignator            = models.TextField(blank=True)
    unitnumber                = models.TextField(blank=True)
    cityname                  = models.TextField(blank=True)
    statecode                 = models.TextField(blank=True)
    zipcode                   = models.TextField(blank=True)
    zip4                      = models.TextField(blank=True)
    phone                     = models.TextField(blank=True)
    phonecode                 = models.TextField(blank=True)
    mailsuppression           = models.TextField(blank=True)
    nosolicitation            = models.TextField(blank=True)
    phonesuppression          = models.TextField(blank=True)
    msa                       = models.TextField(blank=True)
    webaddress                = models.TextField(blank=True)
    adultcontentflag          = models.TextField(blank=True)
    secondphonenumber         = models.TextField(blank=True)
    secondphonenumbercode     = models.TextField(blank=True)
    emailaddress              = models.TextField(blank=True)
    adtype                    = models.TextField(blank=True)
    adsize                    = models.TextField(blank=True)
    creditcardsaccepted       = models.TextField(blank=True)
    freecode                  = models.TextField(blank=True)
    hours                     = models.TextField(blank=True)
    language                  = models.TextField(blank=True)
    discountcode              = models.TextField(blank=True)
    deliverycode              = models.TextField(blank=True)
    yearstarted               = models.TextField(blank=True)
    yearsinbus                = models.TextField(blank=True)
    directions                = models.TextField(blank=True)
    slogans                   = models.TextField(blank=True)
    products                  = models.TextField(blank=True)
    productssynonyms          = models.TextField(blank=True)
    brands                    = models.TextField(blank=True)
    brandssynonyms            = models.TextField(blank=True)
    trademark                 = models.TextField(blank=True)
    services                  = models.TextField(blank=True)
    servicessynonyms          = models.TextField(blank=True)
    modelsfield               = models.TextField(blank=True)
    modelssynonyms            = models.TextField(blank=True)
    specialties               = models.TextField(blank=True)
    specialtiessynonyms       = models.TextField(blank=True)
    programsoffered           = models.TextField(blank=True)
    programsofferedsynonyms   = models.TextField(blank=True)
    productfeatures           = models.TextField(blank=True)
    productfeaturessynonyms   = models.TextField(blank=True)
    servicefeatures           = models.TextField(blank=True)
    servicefeaturessynonyms   = models.TextField(blank=True)
    locationfeatures          = models.TextField(blank=True)
    locationfeaturessynonyms  = models.TextField(blank=True)
    groupsserved              = models.TextField(blank=True)
    groupsservedsynonyms      = models.TextField(blank=True)
    industrytype              = models.TextField(blank=True)
    industrytypesynonyms      = models.TextField(blank=True)
    specialconsiderations     = models.TextField(blank=True)
    specialconsiderationssynonyms = models.TextField(blank=True)
    specialhours              = models.TextField(blank=True)
    specialhourssynonyms      = models.TextField(blank=True)
    orderingmethods           = models.TextField(blank=True)
    orderingmethodssynonyms   = models.TextField(blank=True)
    professionalsonstaff      = models.TextField(blank=True)
    professionalsonstaffsynonyms = models.TextField(blank=True)
    paymentmode               = models.TextField(blank=True)
    paymentmodesynonyms       = models.TextField(blank=True)
    associations              = models.TextField(blank=True)
    associationssynonyms      = models.TextField(blank=True)
    certifications            = models.TextField(blank=True)
    certificationssynonyms    = models.TextField(blank=True)
    generalcontent            = models.TextField(blank=True)
    generalcontentsynonyms    = models.TextField(blank=True)
    businesslink              = models.TextField(blank=True)
    primarybusinessclassificationflag = models.TextField(blank=True)
    syph1                     = models.TextField(blank=True)
    syph2                     = models.TextField(blank=True)
    syph3                     = models.TextField(blank=True)
    syph4                     = models.TextField(blank=True)
    syph5                     = models.TextField(blank=True)
    syph6                     = models.TextField(blank=True)
    sic1                      = models.TextField(blank=True)
    sic2                      = models.TextField(blank=True)
    sic3                      = models.TextField(blank=True)
    sic4                      = models.TextField(blank=True)
    sic5                      = models.TextField(blank=True)
    sic6                      = models.TextField(blank=True)
    naics1                    = models.TextField(blank=True)
    naics2                    = models.TextField(blank=True)
    naics3                    = models.TextField(blank=True)
    naics4                    = models.TextField(blank=True)
    naics5                    = models.TextField(blank=True)
    naics6                    = models.TextField(blank=True)
    bdc1                      = models.TextField(blank=True)
    bdc2                      = models.TextField(blank=True)
    bdc3                      = models.TextField(blank=True)
    bdc4                      = models.TextField(blank=True)
    bdc5                      = models.TextField(blank=True)
    bdc6                      = models.TextField(blank=True)
    fax                       = models.TextField(blank=True)
    ageofrecord               = models.TextField(blank=True)
    addressprivacyflag        = models.TextField(blank=True)
    servicearea               = models.TextField(blank=True)
    chainid                   = models.TextField(blank=True)
    cbsa                      = models.TextField(blank=True)

	
	
################################
#### Transition from SQL Server
class AdvertiserStores(models.Model):
    openx_account_id      = models.TextField(db_index=True)
    acxiom_recordid       = models.TextField(blank=True)
    acxiom_masterrecordid = models.TextField(blank=True, db_index=True)


class PublisherMobileApp(models.Model):
    applicationname = models.TextField(db_index=True)
    appstoreurl     = models.TextField(null=True, blank=True)
    playstoreurl    = models.TextField(null=True, blank=True)
    marketplaceurl  = models.TextField(null=True, blank=True)
    appcategories   = models.TextField(null=True, blank=True)
    gendertarget    = models.TextField(null=True, blank=True)
    ethnicity       = models.TextField(null=True, blank=True)
    age             = models.TextField(null=True, blank=True)
    income          = models.TextField(null=True, blank=True)
    notes           = models.TextField(null=True, blank=True)
    publisherid     = models.TextField(db_index=True)


class PublisherWebApp(models.Model):
    websitename      = models.TextField(db_index=True)
    websiteurl       = models.TextField(null=True, blank=True)
    categoryfilters  = models.TextField(null=True, blank=True)
    gendertargetting = models.TextField(null=True, blank=True)
    ethnicity        = models.TextField(null=True, blank=True)
    age              = models.TextField(null=True, blank=True)
    income           = models.TextField(null=True, blank=True)
    notes            = models.TextField(null=True, blank=True)
    publisherid      = models.TextField(db_index=True)


class PublisherCompanyDetails(models.Model):
    owner_name               = models.TextField(null=True, blank=True)
    company_name             = models.TextField(null=True, blank=True)
    address                  = models.TextField(null=True, blank=True)
    city                     = models.TextField(null=True, blank=True)
    state                    = models.TextField(null=True, blank=True)
    zipcode                  = models.TextField(null=True, blank=True)
    phone_number             = models.TextField(null=True, blank=True)
    montavo_ad_network_optin = models.NullBooleanField()
    publisherid              = models.TextField(db_index=True)


class UserFavoriteDeals(models.Model):
    user_id         = models.TextField(db_index=True)
    advertiser_id   = models.IntegerField()
    advertiser_name = models.TextField(null=True, blank=True)

# address,City,State,ZipCode,CompanyPhoneNumber,PublisherUserRoleId,FirstName,LastName,Email,Notes,CompanyName
