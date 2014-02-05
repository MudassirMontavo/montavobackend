from django.contrib.auth.models import User, Group
from rest_framework import serializers
from spendata.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class AcxiomDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AcxiomData

class MobileAppUserDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MobileAppUserData

class MobileAppMobileDataSerializer(serializers.HyperlinkedModelSerializer):
    mobile_user = MobileAppUserDataSerializer(required=False, read_only=True)

    class Meta:
        model = MobileAppMobileData

class MobileAppLocationDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MobileAppLocationData

class MobileAppUserHomeCircleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MobileAppUserHomeCircle


# OpenX Data Serializers        
class OpenXAccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OpenXAccount

class OpenXUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OpenXUser

class OpenXUserEmailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OpenXUserEmail

class OpenXRoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OpenXRole

class OpenXSiteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OpenXSite

class OpenXAdunitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OpenXAdunit

class OpenXAdunitgroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OpenXAdunitgroup

class OpenXOrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OpenXOrder

class OpenXLineitemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OpenXLineitem

class OpenXAdSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OpenXAd

class OpenXCreativeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OpenXCreative

class OpenXRuleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OpenXRule

class OpenXReportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OpenXReport
        
# ELF Data
class ELFRequestDataSerializer(serializers.HyperlinkedModelSerializer):
    mobile_device = MobileAppMobileDataSerializer(required=False, read_only=True)

    class Meta:
        model = ELFRequestData

class ELFClickDataSerializer(serializers.HyperlinkedModelSerializer):
    mobile_device = MobileAppMobileDataSerializer(required=False, read_only=True)

    class Meta:
        model = ELFClickData

class ELFImpressionDataSerializer(serializers.HyperlinkedModelSerializer):
    mobile_device = MobileAppMobileDataSerializer(required=False, read_only=True)

    class Meta:
        model = ELFImpressionData

class ELFConversionDataSerializer(serializers.HyperlinkedModelSerializer):
    mobile_device = MobileAppMobileDataSerializer(required=False, read_only=True)

    class Meta:
        model = ELFConversionData

# Acxiom Data
class AcxiomBdfGroupsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AcxiomBdfGroups

class AcxiomBdfIndexSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AcxiomBdfIndex

class AcxiomBdfOrgsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AcxiomBdfOrgs

class AcxiomBdfPrimarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AcxiomBdfPrimary

class AcxiomBdfPrimaryBusinessNameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AcxiomBdfPrimaryBusinessName

class AcxiomEbdfOrdSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AcxiomEbdfOrd

################################
#### Transition from SQL Server
class AdvertiserStoresSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AdvertiserStores
		
class PublisherMobileAppSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PublisherMobileApp
		
class PublisherWebAppSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PublisherWebApp

class PublisherCompanyDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PublisherCompanyDetails

class UserFavoriteDealsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserFavoriteDeals

class OpenXAdTargetingIndexSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OpenXAdTargetingIndex