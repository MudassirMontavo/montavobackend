# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AcxiomData'
        db.create_table(u'spendata_acxiomdata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('display_name', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('business_name', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('corporate_name', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('street_number', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('street_directional', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('street_name', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('street_suffix', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('post_directional', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('unit_designator', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('unit_number', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('city_name', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('state_code', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('zip_code', self.gf('django.db.models.fields.TextField')(null=True)),
            ('latitude', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('longitude', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'spendata', ['AcxiomData'])

        # Adding model 'MobileAppUserData'
        db.create_table(u'spendata_mobileappuserdata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('first_name', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('last_name', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('mobile_number', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('gender', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('user_city', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('user_state', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('user_zip', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('user_country', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('user_email', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('income_range', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('age_range', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('area_code', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'spendata', ['MobileAppUserData'])

        # Adding model 'MobileAppMobileData'
        db.create_table(u'spendata_mobileappmobiledata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_data', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['spendata.MobileAppUserData'])),
            ('device_id', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('wireless_carrier', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('device_manufacturer', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('device_model', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'spendata', ['MobileAppMobileData'])

        # Adding model 'MobileAppLocationData'
        db.create_table(u'spendata_mobileapplocationdata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('device_data', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['spendata.MobileAppMobileData'])),
            ('user_latitude', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('user_longitude', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('capture_time_utc', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'spendata', ['MobileAppLocationData'])

        # Adding model 'ELFDataRequestImpressionClick'
        db.create_table(u'spendata_elfdatarequestimpressionclick', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('transaction_id', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('transaction_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('user_id', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('user_id_new', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('publisher_id', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('site_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('ad_unit_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('ad_unit_grp_id', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('ad_width', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('ad_height', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('page_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('delivery_medium_id', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('site_section_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('content_type_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('content_topic_id', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('screen_location_id', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('advertiser_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('order_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('line_item_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('ad_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('is_companion', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_auto_refresh', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_fallback_ad', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_pre_fetch', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('user_ip_address', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('user_latitude', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('user_longitude', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('user_continent', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('user_country', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('user_state', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('user_dma', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('user_msa', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('user_city', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('user_zip', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('user_connection_speed', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('user_connection_type', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('user_device', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('mobile_carrier', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('mobile_net_type', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('user_screen_res', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('user_agent', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('browser_name', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('browser_version', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('user_operating_system', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('user_os_version', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('browser_language', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('page_url', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('referrer_url', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('matched_targeting', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('custom_fields', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('audience_segments', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('traffic_rejected', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'spendata', ['ELFDataRequestImpressionClick'])

        # Adding model 'ELFDataConversion'
        db.create_table(u'spendata_elfdataconversion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('transaction_id', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('transaction_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('user_id', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('user_id_new', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('ad_unit_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('ad_unit_grp_id', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('line_item_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('page_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('beacon_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('is_click', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('ad_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('action_type', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('user_ip_address', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('user_latitude', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('user_longitude', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('user_continent', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('user_country', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('user_state', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('user_dma', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('user_msa', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('user_city', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('user_zip', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('user_connection_speed', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('user_connection_type', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('user_agent', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('user_device', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('mobile_carrier', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('mobile_net_type', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('browser_name', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('browser_version', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('user_operating_system', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('user_os_version', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('browser_language', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('page_url', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('referrer_url', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('custom_fields', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('audience_segments', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('traffic_rejected', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'spendata', ['ELFDataConversion'])


    def backwards(self, orm):
        # Deleting model 'AcxiomData'
        db.delete_table(u'spendata_acxiomdata')

        # Deleting model 'MobileAppUserData'
        db.delete_table(u'spendata_mobileappuserdata')

        # Deleting model 'MobileAppMobileData'
        db.delete_table(u'spendata_mobileappmobiledata')

        # Deleting model 'MobileAppLocationData'
        db.delete_table(u'spendata_mobileapplocationdata')

        # Deleting model 'ELFDataRequestImpressionClick'
        db.delete_table(u'spendata_elfdatarequestimpressionclick')

        # Deleting model 'ELFDataConversion'
        db.delete_table(u'spendata_elfdataconversion')


    models = {
        u'spendata.acxiomdata': {
            'Meta': {'object_name': 'AcxiomData'},
            'business_name': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'city_name': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'corporate_name': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'display_name': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'post_directional': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'state_code': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'street_directional': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'street_name': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'street_number': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'street_suffix': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'unit_designator': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'unit_number': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'zip_code': ('django.db.models.fields.TextField', [], {'null': 'True'})
        },
        u'spendata.elfdataconversion': {
            'Meta': {'object_name': 'ELFDataConversion'},
            'action_type': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'ad_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ad_unit_grp_id': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'ad_unit_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'audience_segments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'beacon_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'browser_language': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'browser_name': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'browser_version': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'custom_fields': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'event_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_click': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'line_item_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mobile_carrier': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'mobile_net_type': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'page_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_url': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'referrer_url': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'traffic_rejected': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'transaction_id': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'transaction_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'user_agent': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'user_city': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'user_connection_speed': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'user_connection_type': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'user_continent': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'user_country': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'user_device': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'user_dma': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'user_id': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'user_id_new': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user_ip_address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'user_latitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'user_longitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'user_msa': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'user_operating_system': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'user_os_version': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'user_state': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'user_zip': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'spendata.elfdatarequestimpressionclick': {
            'Meta': {'object_name': 'ELFDataRequestImpressionClick'},
            'ad_height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ad_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ad_unit_grp_id': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'ad_unit_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ad_width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'advertiser_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'audience_segments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'browser_language': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'browser_name': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'browser_version': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'content_topic_id': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'content_type_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'custom_fields': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'delivery_medium_id': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'event_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_auto_refresh': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_companion': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_fallback_ad': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_pre_fetch': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'line_item_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'matched_targeting': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'mobile_carrier': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'mobile_net_type': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'order_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_url': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'publisher_id': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'referrer_url': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'screen_location_id': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'site_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'site_section_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'traffic_rejected': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'transaction_id': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'transaction_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'user_agent': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'user_city': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'user_connection_speed': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'user_connection_type': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'user_continent': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'user_country': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'user_device': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'user_dma': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'user_id': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'user_id_new': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user_ip_address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'user_latitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'user_longitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'user_msa': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'user_operating_system': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'user_os_version': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'user_screen_res': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'user_state': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'user_zip': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'spendata.mobileapplocationdata': {
            'Meta': {'object_name': 'MobileAppLocationData'},
            'capture_time_utc': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'device_data': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['spendata.MobileAppMobileData']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user_latitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'user_longitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'spendata.mobileappmobiledata': {
            'Meta': {'object_name': 'MobileAppMobileData'},
            'device_id': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'device_manufacturer': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'device_model': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user_data': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['spendata.MobileAppUserData']"}),
            'wireless_carrier': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'spendata.mobileappuserdata': {
            'Meta': {'object_name': 'MobileAppUserData'},
            'age_range': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'area_code': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'first_name': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'gender': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'income_range': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'last_name': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'mobile_number': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'user_city': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'user_country': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'user_email': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'user_id': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'user_state': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'user_zip': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['spendata']