from django.conf.urls import patterns, include, url
from rest_framework import routers
from spendata import views

router = routers.DefaultRouter()
# no need for these at the moment
#router.register(r'users', views.UserViewSet)
#router.register(r'groups', views.GroupViewSet)
router.register(r'acxiom', views.AcxiomDataViewSet)
router.register(r'mobile_user', views.MobileAppUserDataViewSet)
router.register(r'mobile_data', views.MobileAppMobileDataViewSet)
router.register(r'mobile_location', views.MobileAppLocationDataViewSet)

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'spendometer.views.home', name='home'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-docs/', include('rest_framework_swagger.urls')),
)
