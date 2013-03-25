# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        # Note: Remember to use orm['appname.ModelName'] rather than "from appname.models..."

    def backwards(self, orm):
        "Write your backwards methods here."

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'relayapp.company': {
            'Meta': {'object_name': 'Company'},
            'captain': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['relayapp.Participant']", 'null': 'True', 'blank': 'True'}),
            'company_type': ('django.db.models.fields.CharField', [], {'default': "'RT'", 'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'total_people_in_chapter': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'})
        },
        'relayapp.company_registration_record': {
            'Meta': {'object_name': 'Company_Registration_Record'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['relayapp.Company']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'registration_milestone': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['relayapp.Company_Registration_Rule']"})
        },
        'relayapp.company_registration_rule': {
            'Meta': {'object_name': 'Company_Registration_Rule'},
            'candles_rewarded': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'date_cutoff': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'percent_registered': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'})
        },
        'relayapp.company_tshirt_milestone': {
            'Meta': {'object_name': 'Company_TShirt_Milestone'},
            'candles_rewarded': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'percentage_purchased': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'})
        },
        'relayapp.company_tshirt_milestone_record': {
            'Meta': {'object_name': 'Company_TShirt_Milestone_Record'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['relayapp.Company']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tshirt_milestone': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['relayapp.Company_TShirt_Milestone']"})
        },
        'relayapp.donation': {
            'Meta': {'object_name': 'Donation'},
            'amount': ('django.db.models.fields.DecimalField', [], {'default': "'0.00'", 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['relayapp.Participant']"})
        },
        'relayapp.donation_milestone': {
            'Meta': {'ordering': "['candles_rewarded']", 'object_name': 'Donation_Milestone'},
            'candles_rewarded': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'donation_amount': ('django.db.models.fields.DecimalField', [], {'default': "'0.00'", 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'relayapp.email_rule': {
            'Meta': {'object_name': 'Email_Rule'},
            'candles_rewarded': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'emails': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'relayapp.event': {
            'Meta': {'ordering': "['date']", 'object_name': 'Event'},
            'candles_rewarded': ('django.db.models.fields.IntegerField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'homepage': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'relayapp.fundraising_challenge': {
            'Meta': {'object_name': 'Fundraising_Challenge'},
            'amount_raised': ('django.db.models.fields.DecimalField', [], {'default': "'0.00'", 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'candles_raised': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'candles_rewarded': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'datetime_end': ('django.db.models.fields.DateTimeField', [], {}),
            'datetime_start': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'homepage': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'relayapp.fundraising_challenge_record': {
            'Meta': {'object_name': 'Fundraising_Challenge_Record'},
            'candles_rewarded': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'challenge': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['relayapp.Fundraising_Challenge']"}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['relayapp.Participant']"})
        },
        'relayapp.fundraising_challenge_start_record': {
            'Meta': {'object_name': 'Fundraising_Challenge_Start_Record'},
            'amount_raised': ('django.db.models.fields.DecimalField', [], {'default': "'0.00'", 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'candles_raised': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'challenge': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['relayapp.Fundraising_Challenge']"}),
            'datetime_start': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['relayapp.Participant']"})
        },
        'relayapp.fundraising_challenge_tracker_record': {
            'Meta': {'object_name': 'Fundraising_Challenge_Tracker_Record'},
            'challenge': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['relayapp.Fundraising_Challenge']"}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'difference_candles': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'difference_raised': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['relayapp.Participant']"})
        },
        'relayapp.olympics_lap_counter_signup': {
            'Meta': {'object_name': 'Olympics_Lap_Counter_Signup'},
            'captain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'captain_email': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['relayapp.Company']"}),
            'counter': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'olympics': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['relayapp.Team']"}),
            'tier': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'relayapp.participant': {
            'Meta': {'ordering': "['lname', 'fname']", 'object_name': 'Participant'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'emails_sent': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            'facebook_username': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '100'}),
            'fname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'hokie_passport_id': ('django.db.models.fields.BigIntegerField', [], {'default': '0', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'reg_date': ('django.db.models.fields.DateField', [], {}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['relayapp.Team']"})
        },
        'relayapp.participant_email_record': {
            'Meta': {'object_name': 'Participant_Email_Record'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'email_milestone': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['relayapp.Email_Rule']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['relayapp.Participant']"})
        },
        'relayapp.participant_event_record': {
            'Meta': {'object_name': 'Participant_Event_Record'},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['relayapp.Event']"}),
            'guests': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            'hokie_passport_id': ('django.db.models.fields.BigIntegerField', [], {'default': '0', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['relayapp.Participant']"})
        },
        'relayapp.participant_milestone_record': {
            'Meta': {'object_name': 'Participant_Milestone_Record'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'donation_milestone': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['relayapp.Donation_Milestone']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['relayapp.Participant']"})
        },
        'relayapp.participant_tshirt_purchase_record': {
            'Meta': {'object_name': 'Participant_TShirt_Purchase_Record'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['relayapp.Participant']"}),
            'quantity': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            'tshirt': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['relayapp.TShirt']"})
        },
        'relayapp.pledge': {
            'Meta': {'object_name': 'Pledge'},
            'datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_pledge_amount': ('django.db.models.fields.DecimalField', [], {'default': "'0.00'", 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'participant': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['relayapp.Participant']", 'null': 'True', 'blank': 'True'}),
            'pledge_amount': ('django.db.models.fields.DecimalField', [], {'default': "'0.00'", 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'sponsor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'relayapp.team': {
            'Meta': {'ordering': "['name']", 'object_name': 'Team'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['relayapp.Company']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'signup': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'relayapp.team_captain': {
            'Meta': {'object_name': 'Team_Captain'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'fname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'reg_date': ('django.db.models.fields.DateField', [], {}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['relayapp.Team']"})
        },
        'relayapp.team_event_record': {
            'Meta': {'object_name': 'Team_Event_Record'},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['relayapp.Event']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['relayapp.Team']"})
        },
        'relayapp.tshirt': {
            'Meta': {'object_name': 'TShirt'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['relayapp']
    symmetrical = True
