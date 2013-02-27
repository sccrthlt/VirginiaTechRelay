# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Company'
        db.create_table('relayapp_company', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('captain', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['relayapp.Participant'], null=True, blank=True)),
            ('total_people_in_chapter', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, blank=True)),
            ('company_type', self.gf('django.db.models.fields.CharField')(default='RT', max_length=2)),
        ))
        db.send_create_signal('relayapp', ['Company'])

        # Adding model 'Team'
        db.create_table('relayapp_team', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['relayapp.Company'])),
            ('signup', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('relayapp', ['Team'])

        # Adding model 'Participant'
        db.create_table('relayapp_participant', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fname', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('lname', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('emails_sent', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, blank=True)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['relayapp.Team'])),
            ('reg_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('relayapp', ['Participant'])

        # Adding model 'Event'
        db.create_table('relayapp_event', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('candles_rewarded', self.gf('django.db.models.fields.IntegerField')()),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('image', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('homepage', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('relayapp', ['Event'])

        # Adding model 'TShirt'
        db.create_table('relayapp_tshirt', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('relayapp', ['TShirt'])

        # Adding model 'Donation'
        db.create_table('relayapp_donation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('participant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['relayapp.Participant'])),
            ('amount', self.gf('django.db.models.fields.DecimalField')(default='0.00', max_digits=10, decimal_places=2, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('relayapp', ['Donation'])

        # Adding model 'Company_TShirt_Milestone'
        db.create_table('relayapp_company_tshirt_milestone', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('percentage_purchased', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, blank=True)),
            ('candles_rewarded', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('relayapp', ['Company_TShirt_Milestone'])

        # Adding model 'Donation_Milestone'
        db.create_table('relayapp_donation_milestone', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('donation_amount', self.gf('django.db.models.fields.DecimalField')(default='0.00', max_digits=10, decimal_places=2, blank=True)),
            ('candles_rewarded', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('relayapp', ['Donation_Milestone'])

        # Adding model 'Company_Registration_Rule'
        db.create_table('relayapp_company_registration_rule', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('percent_registered', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, blank=True)),
            ('candles_rewarded', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('date_cutoff', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('relayapp', ['Company_Registration_Rule'])

        # Adding model 'Email_Rule'
        db.create_table('relayapp_email_rule', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('candles_rewarded', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('emails', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('relayapp', ['Email_Rule'])

        # Adding model 'Participant_Email_Record'
        db.create_table('relayapp_participant_email_record', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('participant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['relayapp.Participant'])),
            ('email_milestone', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['relayapp.Email_Rule'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('relayapp', ['Participant_Email_Record'])

        # Adding model 'Participant_Event_Record'
        db.create_table('relayapp_participant_event_record', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('guests', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, blank=True)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['relayapp.Event'])),
            ('participant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['relayapp.Participant'])),
        ))
        db.send_create_signal('relayapp', ['Participant_Event_Record'])

        # Adding model 'Company_TShirt_Milestone_Record'
        db.create_table('relayapp_company_tshirt_milestone_record', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['relayapp.Company'])),
            ('tshirt_milestone', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['relayapp.Company_TShirt_Milestone'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('relayapp', ['Company_TShirt_Milestone_Record'])

        # Adding model 'Team_Event_Record'
        db.create_table('relayapp_team_event_record', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['relayapp.Event'])),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['relayapp.Team'])),
        ))
        db.send_create_signal('relayapp', ['Team_Event_Record'])

        # Adding model 'Participant_Milestone_Record'
        db.create_table('relayapp_participant_milestone_record', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('participant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['relayapp.Participant'])),
            ('donation_milestone', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['relayapp.Donation_Milestone'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('relayapp', ['Participant_Milestone_Record'])

        # Adding model 'Participant_TShirt_Purchase_Record'
        db.create_table('relayapp_participant_tshirt_purchase_record', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('participant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['relayapp.Participant'])),
            ('tshirt', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['relayapp.TShirt'])),
            ('quantity', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('relayapp', ['Participant_TShirt_Purchase_Record'])

        # Adding model 'Company_Registration_Record'
        db.create_table('relayapp_company_registration_record', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['relayapp.Company'])),
            ('registration_milestone', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['relayapp.Company_Registration_Rule'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('relayapp', ['Company_Registration_Record'])


    def backwards(self, orm):
        # Deleting model 'Company'
        db.delete_table('relayapp_company')

        # Deleting model 'Team'
        db.delete_table('relayapp_team')

        # Deleting model 'Participant'
        db.delete_table('relayapp_participant')

        # Deleting model 'Event'
        db.delete_table('relayapp_event')

        # Deleting model 'TShirt'
        db.delete_table('relayapp_tshirt')

        # Deleting model 'Donation'
        db.delete_table('relayapp_donation')

        # Deleting model 'Company_TShirt_Milestone'
        db.delete_table('relayapp_company_tshirt_milestone')

        # Deleting model 'Donation_Milestone'
        db.delete_table('relayapp_donation_milestone')

        # Deleting model 'Company_Registration_Rule'
        db.delete_table('relayapp_company_registration_rule')

        # Deleting model 'Email_Rule'
        db.delete_table('relayapp_email_rule')

        # Deleting model 'Participant_Email_Record'
        db.delete_table('relayapp_participant_email_record')

        # Deleting model 'Participant_Event_Record'
        db.delete_table('relayapp_participant_event_record')

        # Deleting model 'Company_TShirt_Milestone_Record'
        db.delete_table('relayapp_company_tshirt_milestone_record')

        # Deleting model 'Team_Event_Record'
        db.delete_table('relayapp_team_event_record')

        # Deleting model 'Participant_Milestone_Record'
        db.delete_table('relayapp_participant_milestone_record')

        # Deleting model 'Participant_TShirt_Purchase_Record'
        db.delete_table('relayapp_participant_tshirt_purchase_record')

        # Deleting model 'Company_Registration_Record'
        db.delete_table('relayapp_company_registration_record')


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
            'date': ('django.db.models.fields.DateField', [], {}),
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
        'relayapp.participant': {
            'Meta': {'ordering': "['lname', 'fname']", 'object_name': 'Participant'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'emails_sent': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            'fname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
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