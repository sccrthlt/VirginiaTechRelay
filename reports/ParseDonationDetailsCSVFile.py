import csv
import os
import time

from django.db.models import Sum
from django.db.models import Max
from datetime import datetime

from relayapp.models import *

def checkDonationsTotals(participant):
    donated = Donation.objects.filter(participant = participant).aggregate(donations_total = Sum('amount'))

    for milestone in Donation_Milestone.objects.all():
        if donated['donations_total'] > milestone.donation_amount:
            try:
                record = Participant_Milestone_Record.objects.get(participant = participant, donation_milestone = milestone)
            except Participant_Milestone_Record.DoesNotExist:
                donated_date = Donation.objects.filter(participant = participant).annotate(most_recent_donation_date = Max('date')) 
                new_participant_milestone_record = Participant_Milestone_Record(participant = participant, donation_milestone = milestone, date = donated_date[0].most_recent_donation_date)
                new_participant_milestone_record.save()

def setupDonation(info):

    try:
        if(info['Email'] == ''):
            info['Email'] = 'no email'
            print('NO EMAIL')
        date_donated = datetime.strptime(info['Donation Date'], '%m/%d/%y %H:%M')
        donation_return = Donation(participant = Participant.objects.get(email = info['Email']), amount = str(float(info['Donation Amount'])), date = date_donated)
        part = Participant.objects.get(email = info['Email'])
        print('Participant: ' + str(part))
        donation_return.save()

        checkDonationsTotals(Participant.objects.get(email = info['Email']))
        
    except Participant.DoesNotExist:
        
        try:
            date_donated = datetime.strptime(info['Donation Date'], '%m/%d/%y %H:%M')

            participants = Participant.objects.filter(fname = info['Participant Credited First Name'], lname = info['Participant Credited Last Name'])            
            if len(participants) > 1:
                l = list(participants[:1])
                found_participant = l[0]
            else:
                found_participant = Participant.objects.get(fname = info['Participant Credited First Name'], lname = info['Participant Credited Last Name'])
            print('Participant2: ' + str(found_participant))
            donation_return = Donation(participant = found_participant, amount = str(float(info['Donation Amount'])), date = date_donated)
            donation_return.save()

            checkDonationsTotals(Participant.objects.get(email = found_participant.email))
            
        except Participant.DoesNotExist:
            print('ERROR: PARTICIPANT NOT FOUND')

def parseCSVPDonationDetails():
    Donation.objects.all().delete()
    with open('DonationDetails.csv', 'rt') as csvfile:
        relayreader = csv.DictReader(csvfile, delimiter=',')
        
        for row in relayreader:

            print (row)

            try:
                #row['Team Name'].decode('ascii')
                if not len(row['Participant Credited Last Name']) == 0 and not len(row['Participant Credited First Name']) == 0:
                    setupDonation(row)
                else:
                    print('SKIPPED')

            except UnicodeDecodeError:
                print ("it was not a ascii-encoded unicode string")

            print ('\n')
