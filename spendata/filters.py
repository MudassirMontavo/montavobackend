import django_filters
from spendata.models import ELFRequestData, ELFImpressionData, ELFClickData, ELFConversionData, MobileAppLocationData, MobileAppUserHomeCircle

class ELFRequestDataFilter(django_filters.FilterSet):
    user_latitude = django_filters.RangeFilter()
    user_longitude = django_filters.RangeFilter()
    class Meta:
        model = ELFRequestData

class ELFImpressionDataFilter(django_filters.FilterSet):
    user_latitude = django_filters.RangeFilter()
    user_longitude = django_filters.RangeFilter()
    class Meta:
        model = ELFImpressionData

class ELFClickDataFilter(django_filters.FilterSet):
    user_latitude = django_filters.RangeFilter()
    user_longitude = django_filters.RangeFilter()
    class Meta:
        model = ELFClickData

class ELFConversionDataFilter(django_filters.FilterSet):
    user_latitude = django_filters.RangeFilter()
    user_longitude = django_filters.RangeFilter()
    class Meta:
        model = ELFConversionData

class MobileAppLocationDataFilter(django_filters.FilterSet):
    user_latitude = django_filters.RangeFilter()
    user_longitude = django_filters.RangeFilter()
    class Meta:
        model = MobileAppLocationData

class MobileAppUserHomeCircleFilter(django_filters.FilterSet):
    latitude = django_filters.RangeFilter()
    longitude = django_filters.RangeFilter()
    class Meta:
        model = MobileAppUserHomeCircle


# We will be creating the logic which allows for the following queries (please add/amend if necessary):
# 1) Give me all imps /clicks and requests for a particular advertiser
#  -- by location
# or for all locations
# 2) Give me all imps/clicks and requests for a particular advertiser which match a user name