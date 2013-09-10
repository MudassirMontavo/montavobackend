# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ELFSerial'
        db.create_table(u'spendata_elfserial', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('serial', self.gf('django.db.models.fields.BigIntegerField')(default=0, null=True, blank=True)),
        ))
        db.send_create_signal(u'spendata', ['ELFSerial'])

        # Adding field 'ELFDataRequestImpressionClick.event_type'
        db.add_column(u'spendata_elfdatarequestimpressionclick', 'event_type',
                      self.gf('django.db.models.fields.CharField')(default='R', max_length=1, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'ELFSerial'
        db.delete_table(u'spendata_elfserial')

        # Deleting field 'ELFDataRequestImpressionClick.event_type'
        db.delete_column(u'spendata_elfdatarequestimpressionclick', 'event_type')


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
            'event_type': ('django.db.models.fields.CharField', [], {'default': "'R'", 'max_length': '1', 'blank': 'True'}),
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
        u'spendata.elfserial': {
            'Meta': {'object_name': 'ELFSerial'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'serial': ('django.db.models.fields.BigIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'})
        },
        u'spendata.mobileapplocationdata': {
            'Meta': {'object_name': 'MobileAppLocationData'},
            'capture_time_utc': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'device_data': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'location_data'", 'null': 'True', 'to': u"orm['spendata.MobileAppMobileData']"}),
            'device_id': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
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
            'user_data': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'mobile_data'", 'null': 'True', 'to': u"orm['spendata.MobileAppUserData']"}),
            'user_id': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
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