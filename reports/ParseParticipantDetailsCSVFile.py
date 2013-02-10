import csv
import os

from relayapp.models import *

def setupParticipant(info):

    try:
        participant_return = Participant.objects.get(email = info['Primary Email Address'])
    except Participant.DoesNotExist:
        try:
            participant_return = Participant(fname = info['First Name'], lname = info['Last Name'], email = info['Primary Email Address'], team = Team.objects.get(name = info['Team Name']))
            participant_return.save()
        except Team.DoesNotExist:
            participant_return = None
            print ('ERROR: USER TEAM DOES NOT EXIST')
            print (info)
            print ('\n')

    return participant_return
                                          

def parseCSVParticipantDetails():
    with open('ParticipantDetails.csv', 'rt') as csvfile:
        relayreader = csv.DictReader(csvfile, delimiter=',')
        
        for row in relayreader:

            try:
                row['Team Name'].decode('ascii')
                setupParticipant(row)

            except UnicodeDecodeError:
                print ("it was not a ascii-encoded unicode string")
                print (row)
                print ('\n')
            
            
