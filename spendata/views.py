from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions

from spendata.models import *
from spendata.serializers import *

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

class MobileAppUserHomeCircleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Acxiom Data to be viewed
    """
    queryset = MobileAppUserHomeCircle.objects.all()
    serializer_class = MobileAppUserHomeCircleSerializer


# OpenX Data
class OpenXAccountViewSet(viewsets.ModelViewSet):
    queryset = OpenXAccount.objects.all()
    serializer_class = OpenXAccountSerializer

class OpenXUserViewSet(viewsets.ModelViewSet):
    queryset = OpenXUser.objects.all()
    serializer_class = OpenXUserSerializer

class OpenXRoleViewSet(viewsets.ModelViewSet):
    queryset = OpenXRole.objects.all()
    serializer_class = OpenXRoleSerializer

class OpenXSiteViewSet(viewsets.ModelViewSet):
    queryset = OpenXSite.objects.all()
    serializer_class = OpenXSiteSerializer

class OpenXAdunitViewSet(viewsets.ModelViewSet):
    queryset = OpenXAdunit.objects.all()
    serializer_class = OpenXAdunitSerializer

class OpenXAdunitgroupViewSet(viewsets.ModelViewSet):
    queryset = OpenXAdunitgroup.objects.all()
    serializer_class = OpenXAdunitgroupSerializer

class OpenXOrderViewSet(viewsets.ModelViewSet):
    queryset = OpenXOrder.objects.all()
    serializer_class = OpenXOrderSerializer

class OpenXLineitemViewSet(viewsets.ModelViewSet):
    queryset = OpenXLineitem.objects.all()
    serializer_class = OpenXLineitemSerializer

class OpenXAdViewSet(viewsets.ModelViewSet):
    queryset = OpenXAd.objects.all()
    serializer_class = OpenXAdSerializer

class OpenXCreativeViewSet(viewsets.ModelViewSet):
    queryset = OpenXCreative.objects.all()
    serializer_class = OpenXCreativeSerializer

class OpenXRuleViewSet(viewsets.ModelViewSet):
    queryset = OpenXRule.objects.all()
    serializer_class = OpenXRuleSerializer

class OpenXReportViewSet(viewsets.ModelViewSet):
    queryset = OpenXReport.objects.all()
    serializer_class = OpenXReportSerializer
    
    
# ELF Data
class ELFRequestDataViewSet(viewsets.ModelViewSet):
    queryset = ELFRequestData.objects.all()
    serializer_class = ELFRequestDataSerializer
    
class ELFClickDataViewSet(viewsets.ModelViewSet):
    queryset = ELFClickData.objects.all()
    serializer_class = ELFClickDataSerializer

class ELFImpressionDataViewSet(viewsets.ModelViewSet):
    queryset = ELFImpressionData.objects.all()
    serializer_class = ELFImpressionDataSerializer

class ELFConversionDataViewSet(viewsets.ModelViewSet):
    queryset = ELFConversionData.objects.all()
    serializer_class = ELFConversionDataSerializer

# Acxiom Data
class AcxiomBdfGroupsViewSet(viewsets.ModelViewSet):
    queryset = AcxiomBdfGroups.objects.all()
    serializer_class = AcxiomBdfGroupsSerializer

class AcxiomBdfIndexViewSet(viewsets.ModelViewSet):
    queryset = AcxiomBdfIndex.objects.all()
    serializer_class = AcxiomBdfIndexSerializer

class AcxiomBdfOrgsViewSet(viewsets.ModelViewSet):
    queryset = AcxiomBdfOrgs.objects.all()
    serializer_class = AcxiomBdfOrgsSerializer

class AcxiomBdfPrimaryViewSet(viewsets.ModelViewSet):
    queryset = AcxiomBdfPrimary.objects.all()
    serializer_class = AcxiomBdfPrimarySerializer

class AcxiomEbdfOrdViewSet(viewsets.ModelViewSet):
    queryset = AcxiomEbdfOrd.objects.all()
    serializer_class = AcxiomEbdfOrdSerializer
