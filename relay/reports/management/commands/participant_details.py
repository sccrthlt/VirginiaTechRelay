from django.core.management.base import BaseCommand, CommandError
import csv
import os
import cStringIO
from datetime import datetime, date, time
from relayapp.models import *
from django.forms.models import model_to_dict
from django.contrib.auth.models import User, Group

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
        #s = model_to_dict(Participant.objects.get(email = info['Primary Email Address']))['id']
        #setupUser(s)
    except Participant.DoesNotExist:
        try:
            participant_return = Participant(
                fname = info['First Name'],
                lname = info['Last Name'],
                email = info['Primary Email Address'],
                team = Team.objects.get(name = info['Team Name']),
                reg_date = datetime.strptime(info['Registration Date'], '%m/%d/%y %H:%M')
            )
            participant_return.save()
            #s = model_to_dict(Participant.objects.get(email = info['Primary Email Address']))['id']
            #setupUser(s)
        except Team.DoesNotExist:
            participant_return = Participant(
                fname = info['First Name'],
                lname = info['Last Name'],
                email = info['Primary Email Address'],
                team = Team.objects.get(name = 'General Team'),
                reg_date = datetime.strptime(info['Registration Date'], '%m/%d/%y %H:%M')
            )
            participant_return.save()
            #s = model_to_dict(Participant.objects.get(email = info['Primary Email Address']))['id']
            #setupUser(s)
            print("Team does not exist for >> "+info['Team Name'])
            print("Put into General Team")

    return participant_return

#def setupUser(info):
	#participant = Participant.objects.get(pk = info)
	#username = participant.pk
	#email = participant.email
	#groups = Group.objects.get(name = 'myCandles')

	#try:
		user = User.objects.get(username = info)
	#except User.DoesNotExist:
		#participant = Participant.objects.get(pk = info)
		#new_user = User.objects.create_user(username = username, email = email, password = 'password')
		#new_user.groups = groups
		#new_user.save()

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
