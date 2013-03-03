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
        parseCSVHokiePassport(csv_file_location)

def setupParticipant(info):

	for event in Event.objects.all()
		try:
			participant_event_return = Participant_Event_Record.objects.get(hokie_passport_id = info['Card Number'], event = event)
		except Participant_Event_Record.DoesNotExist:
			try:
				new_participant_event_record = Participant_Event_Record(
					participant = Participant.objects.get(hokie_passport_id = info['Card Number']),
					id = info['Card Number'],
					event = Event.objects.get(event = event),
				)
				new_participant_event_record.save()
			except len(info['id']) == 0:
				return None

def parseCSVHokiePassport(csv_file_location):

    data = open(csv_file_location).read()
    relayreader = csv.DictReader(cStringIO.StringIO(data), delimiter=',')

    print("starting...")
    for row in relayreader:
        try:
            row['Team Name'] = unicode(row['Team Name'], 'latin-1')
            setupParticipant(row)

        except UnicodeDecodeError:
            print ("it was not a ascii-encoded unicode string")
            print (row)
            print ('\n')
