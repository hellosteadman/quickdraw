# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Donation'
        db.create_table(u'donations_donation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('remote_id', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('live', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('paid', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('currency', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('created', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'donations', ['Donation'])


    def backwards(self, orm):
        # Deleting model 'Donation'
        db.delete_table(u'donations_donation')


    models = {
        u'donations.donation': {
            'Meta': {'object_name': 'Donation'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'currency': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'live': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'paid': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'remote_id': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        }
    }

    complete_apps = ['donations']