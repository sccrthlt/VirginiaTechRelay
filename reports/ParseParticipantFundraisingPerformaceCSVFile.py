import csv
import os
import datetime

from relayapp.models import *

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

        #checkEmailTotals(participant)

    except Participant.DoesNotExist:
        try:
            participant = Participant.objects.get(fname = info['Participant First Name'], lname = info['Participant Last Name'])
            participant.emails_sent = info['Emails Sent']
            participant.save()

            #checkEmailTotals(participant)

        except Participant.DoesNotExist:
            print('ERROR: PARTICIPANT DOES NOT EXIST')

def parseCSVParticipantFundraising():
    Participant_Email_Record.objects.all().delete()
    with open('ParticipantFundraisingPerformance.csv', 'rt') as csvfile:
        relayreader = csv.DictReader(csvfile, delimiter=',')
        for row in relayreader:

            print (row)

            try:
                row['Team Name'].decode('ascii')
                setupEmailsSent(row)

            except UnicodeDecodeError:
                print ("it was not a ascii-encoded unicode string")


            print ('\n')
