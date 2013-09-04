from django.contrib.auth.models import User, Group
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework import permissions
from spendata.serializers import UserSerializer, GroupSerializer, AcxiomDataSerializer, MobileAppUserDataSerializer, MobileAppMobileDataSerializer, MobileAppLocationDataSerializer
from spendata.models import AcxiomData, MobileAppUserData, MobileAppMobileData, MobileAppLocationData

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class AcxiomDataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Acxiom Data to be viewed
    """
    queryset = AcxiomData.objects.all()
    serializer_class = AcxiomDataSerializer

class MobileAppUserDataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows MobileAppUser Data to be viewed
    """
    queryset = MobileAppUserData.objects.all()
    serializer_class = MobileAppUserDataSerializer

class MobileAppMobileDataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Acxiom Data to be viewed
    """
    queryset = MobileAppMobileData.objects.all()
    serializer_class = MobileAppMobileDataSerializer

class MobileAppLocationDataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Acxiom Data to be viewed
    """
    queryset = MobileAppLocationData.objects.all()
    serializer_class = MobileAppLocationDataSerializer