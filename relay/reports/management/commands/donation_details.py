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
    args = 'CSV file with <Donation> detail data'
    help = 'Parses CSV files related to donation details'

    def handle(self, *args, **options):
        print "Starting Command.."
        csv_file_location = args[0]
        parseCSVPDonationDetails(csv_file_location)

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
        date_donated = datetime.strptime(info['Donation Date'], '%m/%d/%y %H:%M')

        participants = Participant.objects.filter(
            fname = info['Participant Credited First Name'],
            lname = info['Participant Credited Last Name']
        )

        if len(participants) > 1:
            l = list(participants[:1])
            found_participant = l[0]
        else:
            found_participant = Participant.objects.get(
                fname = info['Participant Credited First Name'],
                lname = info['Participant Credited Last Name']
            )
        # print('Participant2: ' + str(found_participant))
        donation_return = Donation(participant = found_participant, amount = str(float(info['Donation Amount'])), date = date_donated)
        donation_return.save()

        checkDonationsTotals(Participant.objects.get(email = found_participant.email))

    except Participant.DoesNotExist:
        print('Participant not found for >> ' + info['Participant Credited First Name'] + ' ' + info['Participant Credited Last Name'])

def parseCSVPDonationDetails(csv_file_location):
    Donation.objects.all().delete()
    data = open(csv_file_location).read()
    relayreader = csv.DictReader(cStringIO.StringIO(data), delimiter=',')

    # row['Team Name'].decode('ascii')

    for row in relayreader:
        try:
            if not len(row['Participant Credited Last Name']) == 0 and not len(row['Participant Credited First Name']) == 0:
                setupDonation(row)
            else:
                print('SKIPPED')

        except UnicodeDecodeError:
            print ("it was not a ascii-encoded unicode string")
