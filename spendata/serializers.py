from django.contrib.auth.models import User, Group
from rest_framework import serializers
from spendata.models import AcxiomData, MobileAppUserData, MobileAppMobileData, MobileAppLocationData


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