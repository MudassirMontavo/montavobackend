from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from spendata import views


# REST API stuff
router = routers.DefaultRouter()

# no need for these at the moment
#router.register(r'users', views.UserViewSet)
#router.register(r'groups', views.GroupViewSet)
router.register(r'mobile_user', views.MobileAppUserDataViewSet)
router.register(r'mobile_data', views.MobileAppMobileDataViewSet)
router.register(r'mobile_location', views.MobileAppLocationDataViewSet)
router.register(r'mobile_user_home_circle', views.MobileAppUserHomeCircleViewSet)

router.register(r'openx_account', views.OpenXAccountViewSet)
router.register(r'openx_user', views.OpenXUserViewSet)
router.register(r'openx_role', views.OpenXRoleViewSet)
router.register(r'openx_site', views.OpenXSiteViewSet)
router.register(r'openx_adunit', views.OpenXAdunitViewSet)
router.register(r'openx_adunitgroup', views.OpenXAdunitgroupViewSet)
router.register(r'openx_order', views.OpenXOrderViewSet)
router.register(r'openx_lineitem', views.OpenXLineitemViewSet)
router.register(r'openx_ad', views.OpenXAdViewSet)
router.register(r'openx_creative', views.OpenXCreativeViewSet)
router.register(r'openx_rule', views.OpenXRuleViewSet)
router.register(r'openx_report', views.OpenXReportViewSet)

router.register(r'elf_request', views.ELFRequestDataViewSet)
router.register(r'elf_click', views.ELFClickDataViewSet)
router.register(r'elf_impression', views.ELFImpressionDataViewSet)
router.register(r'elf_conversion', views.ELFConversionDataViewSet)

router.register(r'acxiom_old', views.AcxiomDataViewSet)
router.register(r'acxiom_bdfgroups', views.AcxiomBdfGroupsViewSet)
router.register(r'acxiom_bdfindex', views.AcxiomBdfIndexViewSet)
router.register(r'acxiom_bdforgs', views.AcxiomBdfOrgsViewSet)
router.register(r'acxiom_bdfprimary', views.AcxiomBdfPrimaryViewSet)
router.register(r'acxiom_ebdford', views.AcxiomEbdfOrdViewSet)

################################
#### Transition from SQL Server
router.register(r'advertiser_stores', views.AdvertiserStoresViewSet)
router.register(r'publisher_mobile_app', views.PublisherMobileAppViewSet)
router.register(r'publisher_web_app', views.PublisherWebAppViewSet)
router.register(r'publisher_company_details', views.PublisherCompanyDetailsViewSet)
router.register(r'user_favorite_deals', views.UserFavoriteDealsViewSet)

# Admin stuff
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-docs/', include('rest_framework_swagger.urls')),
    url(r'^', include(router.urls)),
)