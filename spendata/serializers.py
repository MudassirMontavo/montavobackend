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
    class Meta:
        model = MobileAppMobileData
        read_only_fields = ('user_data',)

class MobileAppLocationDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MobileAppLocationData
        read_only_fields = ('device_data',)

class MobileAppUserHomeCircleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MobileAppUserHomeCircle
        read_only_fields = ('user_data',)


# OpenX Data Serializers        
class OpenXAccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OpenXAccount

class OpenXUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OpenXUser

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
    class Meta:
        model = ELFRequestData

class ELFClickDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ELFClickData

class ELFImpressionDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ELFImpressionData

class ELFConversionDataSerializer(serializers.HyperlinkedModelSerializer):
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

class AcxiomEbdfOrdSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AcxiomEbdfOrd
