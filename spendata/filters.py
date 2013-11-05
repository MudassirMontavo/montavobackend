import django_filters
from spendata.models import (
    ELFRequestData, ELFImpressionData, ELFClickData, ELFConversionData,
    MobileAppLocationData, MobileAppUserHomeCircle,
    AcxiomBdfGroups, AcxiomBdfPrimary, AcxiomBdfOrgs
)


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


class AcxiomBdfGroupsFilter(django_filters.FilterSet):
    latitude = django_filters.RangeFilter()
    longitude = django_filters.RangeFilter()

    class Meta:
        model = AcxiomBdfGroups


class AcxiomBdfPrimaryFilter(django_filters.FilterSet):
    latitude = django_filters.RangeFilter()
    longitude = django_filters.RangeFilter()

    class Meta:
        model = AcxiomBdfPrimary


class AcxiomBdfOrgsFilter(django_filters.FilterSet):
    latitude = django_filters.RangeFilter()
    longitude = django_filters.RangeFilter()

    class Meta:
        model = AcxiomBdfOrgs
