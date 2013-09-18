from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions, filters

from spendata.models import *
from spendata.serializers import *
from spendata.filters import *

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
    API endpoint that allows (old) Acxiom Data to be viewed
    """
    queryset = AcxiomData.objects.all()
    serializer_class = AcxiomDataSerializer

class MobileAppUserDataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows MobileAppUser Data to be viewed
    """
    queryset = MobileAppUserData.objects.all()
    serializer_class = MobileAppUserDataSerializer
    filter_fields = MobileAppUserData()._meta.get_all_field_names()

class MobileAppMobileDataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Acxiom Data to be viewed
    """
    queryset = MobileAppMobileData.objects.all()
    serializer_class = MobileAppMobileDataSerializer
    filter_fields = MobileAppMobileData()._meta.get_all_field_names()

class MobileAppLocationDataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Acxiom Data to be viewed
    """
    queryset = MobileAppLocationData.objects.all()
    serializer_class = MobileAppLocationDataSerializer
    filter_fields = MobileAppLocationData()._meta.get_all_field_names()

class MobileAppUserHomeCircleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Acxiom Data to be viewed
    """
    queryset = MobileAppUserHomeCircle.objects.all()
    serializer_class = MobileAppUserHomeCircleSerializer
    filter_fields = MobileAppUserHomeCircle()._meta.get_all_field_names()


# OpenX Data
class OpenXAccountViewSet(viewsets.ModelViewSet):
    queryset = OpenXAccount.objects.all()
    serializer_class = OpenXAccountSerializer
    filter_backends = (filters.SearchFilter, filters.DjangoFilterBackend)
    search_fields = ('name',)
    filter_fields = OpenXAccount()._meta.get_all_field_names()

class OpenXUserViewSet(viewsets.ModelViewSet):
    queryset = OpenXUser.objects.all()
    serializer_class = OpenXUserSerializer
    filter_fields = OpenXUser()._meta.get_all_field_names()

class OpenXRoleViewSet(viewsets.ModelViewSet):
    queryset = OpenXRole.objects.all()
    serializer_class = OpenXRoleSerializer
    filter_fields = OpenXRole()._meta.get_all_field_names()

class OpenXSiteViewSet(viewsets.ModelViewSet):
    queryset = OpenXSite.objects.all()
    serializer_class = OpenXSiteSerializer
    filter_fields = OpenXSite()._meta.get_all_field_names()

class OpenXAdunitViewSet(viewsets.ModelViewSet):
    queryset = OpenXAdunit.objects.all()
    serializer_class = OpenXAdunitSerializer
    filter_fields = OpenXAdunit()._meta.get_all_field_names()

class OpenXAdunitgroupViewSet(viewsets.ModelViewSet):
    queryset = OpenXAdunitgroup.objects.all()
    serializer_class = OpenXAdunitgroupSerializer
    filter_fields = OpenXAdunitgroup()._meta.get_all_field_names()

class OpenXOrderViewSet(viewsets.ModelViewSet):
    queryset = OpenXOrder.objects.all()
    serializer_class = OpenXOrderSerializer
    filter_fields = OpenXOrder()._meta.get_all_field_names()

class OpenXLineitemViewSet(viewsets.ModelViewSet):
    queryset = OpenXLineitem.objects.all()
    serializer_class = OpenXLineitemSerializer
    filter_fields = OpenXLineitem()._meta.get_all_field_names()

class OpenXAdViewSet(viewsets.ModelViewSet):
    queryset = OpenXAd.objects.all()
    serializer_class = OpenXAdSerializer
    filter_fields = OpenXAd()._meta.get_all_field_names()

class OpenXCreativeViewSet(viewsets.ModelViewSet):
    queryset = OpenXCreative.objects.all()
    serializer_class = OpenXCreativeSerializer
    filter_fields = OpenXCreative()._meta.get_all_field_names()

class OpenXRuleViewSet(viewsets.ModelViewSet):
    queryset = OpenXRule.objects.all()
    serializer_class = OpenXRuleSerializer
    filter_fields = OpenXRule()._meta.get_all_field_names()

class OpenXReportViewSet(viewsets.ModelViewSet):
    queryset = OpenXReport.objects.all()
    serializer_class = OpenXReportSerializer
    filter_fields = OpenXReport()._meta.get_all_field_names()
    
# ELF Data
class ELFRequestDataViewSet(viewsets.ModelViewSet):
    queryset = ELFRequestData.objects.all()
    serializer_class = ELFRequestDataSerializer
    filter_class = ELFRequestDataFilter
    
class ELFClickDataViewSet(viewsets.ModelViewSet):
    queryset = ELFClickData.objects.all()
    serializer_class = ELFClickDataSerializer
    filter_class = ELFClickDataFilter

class ELFImpressionDataViewSet(viewsets.ModelViewSet):
    queryset = ELFImpressionData.objects.all()
    serializer_class = ELFImpressionDataSerializer
    filter_class = ELFImpressionDataFilter

class ELFConversionDataViewSet(viewsets.ModelViewSet):
    queryset = ELFConversionData.objects.all()
    serializer_class = ELFConversionDataSerializer
    filter_class = ELFConversionDataFilter

# Acxiom Data
class AcxiomBdfGroupsViewSet(viewsets.ModelViewSet):
    queryset = AcxiomBdfGroups.objects.all()
    serializer_class = AcxiomBdfGroupsSerializer
    filter_fields = AcxiomBdfGroups()._meta.get_all_field_names()

class AcxiomBdfIndexViewSet(viewsets.ModelViewSet):
    queryset = AcxiomBdfIndex.objects.all()
    serializer_class = AcxiomBdfIndexSerializer
    filter_fields = AcxiomBdfIndex()._meta.get_all_field_names()

class AcxiomBdfOrgsViewSet(viewsets.ModelViewSet):
    queryset = AcxiomBdfOrgs.objects.all()
    serializer_class = AcxiomBdfOrgsSerializer
    filter_fields = AcxiomBdfOrgs()._meta.get_all_field_names()

class AcxiomBdfPrimaryViewSet(viewsets.ModelViewSet):
    queryset = AcxiomBdfPrimary.objects.all()
    serializer_class = AcxiomBdfPrimarySerializer
    filter_fields = AcxiomBdfPrimary()._meta.get_all_field_names()

class AcxiomEbdfOrdViewSet(viewsets.ModelViewSet):
    queryset = AcxiomEbdfOrd.objects.all()
    serializer_class = AcxiomEbdfOrdSerializer
    filter_fields = AcxiomEbdfOrd()._meta.get_all_field_names()
