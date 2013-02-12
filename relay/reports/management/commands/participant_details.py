from django.core.management.base import BaseCommand, CommandError
import csv
import os
import cStringIO
from datetime import datetime, date, time
from relayapp.models import *

class Command(BaseCommand):
    args = 'CSV file with <Participant> detail data'
    help = 'Parses CSV files related to participant details'

    def handle(self, *args, **options):
        print "Starting Command.."
        csv_file_location = args[0]
        parseCSVParticipantDetails(csv_file_location)

def setupParticipant(info):

    try:
        participant_return = Participant.objects.get(email = info['Primary Email Address'])
    except Participant.DoesNotExist:
        try:
            participant_return = Participant(
                fname = info['First Name'],
                lname = info['Last Name'],
                email = info['Primary Email Address'],
                team = Team.objects.get(name = info['Team Name'])
                reg_date = datetime.strptime(info['Registration Date'], '%m/%d/%y %H:%M')
            )
            participant_return.save()
        except Team.DoesNotExist:
            participant_return = None
            print("Team does not exist for >> "+info['Team Name'])

    return participant_return

def parseCSVParticipantDetails(csv_file_location):

    data = open(csv_file_location).read()
    relayreader = csv.DictReader(cStringIO.StringIO(data), delimiter=',')

    print("starting...")
    for row in relayreader:
        try:
            row['Team Name'].decode('ascii')
            setupParticipant(row)

        except UnicodeDecodeError:
            print ("it was not a ascii-encoded unicode string")
            print (row)
            print ('\n')