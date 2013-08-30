from django.contrib.auth.models import User, Group
from rest_framework import serializers
from spendata.models import AcxiomData


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