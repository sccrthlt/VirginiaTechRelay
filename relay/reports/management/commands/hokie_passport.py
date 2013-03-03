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

    try:
		events = Participant_Event_Record.objects.all()
		for event_record in events
			participant_event_return = Participant_Event_Record.objects.filter(hokie_passport_id = info['Card Number'])
    except Participant.DoesNotExist:
        try:
			participant_event_return = Participant_Event_Record(
				participant = Participant.objects.get(pk = info['id']),
				id = info['id'],
				event = Event.objects.get(event = eventname),
            )
            participant_return.save()

    return participant_event_return

def parseCSVParticipantDetails(csv_file_location):

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
