# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Exercise'
        db.create_table(u'mission_control_exercise', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('topic', self.gf('django.db.models.fields.related.ForeignKey')(related_name='exercise', to=orm['mission_control.Topic'])),
            ('difficulty', self.gf('django.db.models.fields.CharField')(max_length=120)),
        ))
        db.send_create_signal(u'mission_control', ['Exercise'])

        # Adding model 'Topic'
        db.create_table(u'mission_control_topic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('week', self.gf('django.db.models.fields.IntegerField')()),
            ('day', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('am_pm', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'mission_control', ['Topic'])


    def backwards(self, orm):
        # Deleting model 'Exercise'
        db.delete_table(u'mission_control_exercise')

        # Deleting model 'Topic'
        db.delete_table(u'mission_control_topic')


    models = {
        u'mission_control.exercise': {
            'Meta': {'object_name': 'Exercise'},
            'difficulty': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'topic': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'exercise'", 'to': u"orm['mission_control.Topic']"})
        },
        u'mission_control.topic': {
            'Meta': {'object_name': 'Topic'},
            'am_pm': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'day': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'week': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['mission_control']