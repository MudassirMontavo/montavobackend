from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from spendata.serializers import UserSerializer, GroupSerializer, AcxiomDataSerializer
from spendata.models import AcxiomData

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