# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AllRequest'
        db.create_table(u'hello_allrequest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('cookies_dict', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'hello', ['AllRequest'])


    def backwards(self, orm):
        # Deleting model 'AllRequest'
        db.delete_table(u'hello_allrequest')


    models = {
        u'hello.allrequest': {
            'Meta': {'object_name': 'AllRequest'},
            'cookies_dict': ('django.db.models.fields.TextField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'hello.person': {
            'Meta': {'object_name': 'Person'},
            'bio': ('django.db.models.fields.TextField', [], {}),
            'birthday': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'contacts': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['hello']