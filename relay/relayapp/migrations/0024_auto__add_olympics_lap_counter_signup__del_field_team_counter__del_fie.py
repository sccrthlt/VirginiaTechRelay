# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Olympics_Lap_Counter_Signup'
        db.create_table('relayapp_olympics_lap_counter_signup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['relayapp.Team'])),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['relayapp.Company'])),
            ('captain', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('captain_email', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('olympics', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('counter', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')(default=None, null=True, blank=True)),
        ))
        db.send_create_signal('relayapp', ['Olympics_Lap_Counter_Signup'])

        # Deleting field 'Team.counter'
        db.delete_column('relayapp_team', 'counter')

        # Deleting field 'Team.counter_datetime'
        db.delete_column('relayapp_team', 'counter_datetime')


    def backwards(self, orm):
        # Deleting model 'Olympics_Lap_Counter_Signup'
        db.delete_table('relayapp_olympics_lap_counter_signup')

        # Adding field 'Team.counter'
        db.add_column('relayapp_team', 'counter',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Team.counter_datetime'
        db.add_column('relayapp_team', 'counter_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=None, null=True, blank=True),
                      keep_default=False)


    models = {
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
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['relayapp.Team']"})
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
        'relayapp.team': {
            'Meta': {'ordering': "['name']", 'object_name': 'Team'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['relayapp.Company']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'signup': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
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