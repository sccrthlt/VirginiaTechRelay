from django.core.management.base import BaseCommand, CommandError
import csv
import os
import time
import cStringIO

from django.db.models import Sum
from django.db.models import Max
from datetime import datetime

from relayapp.models import *

class Command(BaseCommand):
    args = 'CSV file with <Participant Fundraising> detail data'
    help = 'Parses CSV files related to participant Fundraising'

    def handle(self, *args, **options):
        print "Starting Command.."
        csv_file_location = args[0]
        parseCSVParticipantFundraising(csv_file_location)

def checkEmailTotals(participant):

    emails_count = participant.emails_sent

    for milestone in Email_Rule.objects.all():
	if int(emails_count) > int(milestone.emails):
	    print('Email Count: ' + str(emails_count) + ' Milestone Emails: ' + str(milestone.emails))
	    try:
		record = Participant_Email_Record.objects.get(participant = participant, email_milestone = milestone)
	    except Participant_Email_Record.DoesNotExist:
		date = now = datetime.datetime.now()
		new_participant_email_record = Participant_Email_Record(participant = participant, email_milestone = milestone, date = date)
		new_participant_email_record.save()

def setupEmailsSent(info):

    try:
	participant = Participant.objects.get(email = info['Participant Email'])
	participant.emails_sent = info['Emails Sent']
	participant.save()

	checkEmailTotals(participant)

    except Participant.DoesNotExist:
	try:
	    participant = Participant.objects.get(fname = info['Participant First Name'], lname = info['Participant Last Name'])
	    participant.emails_sent = info['Emails Sent']
	    participant.save()

	    checkEmailTotals(participant)

	except Participant.DoesNotExist:
                print('ERROR: PARTICIPANT DOES NOT EXIST')
                print info

def parseCSVParticipantFundraising(csv_file_location):
    data = open(csv_file_location).read()
    relayreader = csv.DictReader(cStringIO.StringIO(data), delimiter=',')
    for row in relayreader:
        # print (row)
        try:
            row['Team Name'] = unicode(row['Team Name'], 'latin-1')
            setupEmailsSent(row)

        except UnicodeDecodeError:
            print ("it was not a ascii-encoded unicode string")
