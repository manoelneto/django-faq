# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Question.updated_by'
        db.delete_column(u'faq_question', 'updated_by_id')

        # Deleting field 'Question.sort_order'
        db.delete_column(u'faq_question', 'sort_order')

        # Deleting field 'Question.protected'
        db.delete_column(u'faq_question', 'protected')

        # Deleting field 'Question.created_by'
        db.delete_column(u'faq_question', 'created_by_id')


        # Changing field 'Question.topic'
        db.alter_column(u'faq_question', 'topic_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['faq.Topic']))
        # Deleting field 'Topic.sort_order'
        db.delete_column(u'faq_topic', 'sort_order')


    def backwards(self, orm):
        # Adding field 'Question.updated_by'
        db.add_column(u'faq_question', 'updated_by',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', null=True, to=orm['auth.User']),
                      keep_default=False)

        # Adding field 'Question.sort_order'
        db.add_column(u'faq_question', 'sort_order',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Question.protected'
        db.add_column(u'faq_question', 'protected',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Question.created_by'
        db.add_column(u'faq_question', 'created_by',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', null=True, to=orm['auth.User']),
                      keep_default=False)


        # Changing field 'Question.topic'
        db.alter_column(u'faq_question', 'topic_id', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['faq.Topic']))
        # Adding field 'Topic.sort_order'
        db.add_column(u'faq_topic', 'sort_order',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    models = {
        u'faq.question': {
            'Meta': {'ordering': "['created_on']", 'object_name': 'Question'},
            'answer': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'topic': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'questions'", 'null': 'True', 'to': u"orm['faq.Topic']"}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'faq.topic': {
            'Meta': {'ordering': "['name']", 'object_name': 'Topic'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        }
    }

    complete_apps = ['faq']