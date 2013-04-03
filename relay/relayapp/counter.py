import csv
import os
import sys
import cStringIO
from datetime import datetime, date, time
import datetime
from relayapp.models import *
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def upload_file(request):

	if request.method == 'POST':
		csv_file = request.FILES['test']
		parseCSVCounter(csv_file)
		return HttpResponse(status=400)
	else:
		return HttpResponse(status=400)
	return render_to_response('base.html', {'form': form})

def parseCSVCounter(csv_file):

    paramFile = csv_file.read()
    #portfolio = csv.DictReader(paramFile)
    #data = open(csv_file).read()
    relayreader = csv.DictReader(cStringIO.StringIO(paramFile), delimiter=',')

    for row in relayreader:

        try:
            row['Team Name'] = unicode(row['Team Name'], 'latin-1')

            company = setupCompany(row)

        except UnicodeDecodeError, e:
            print e

        except Exception, e:
            print e
	
	event = Event.objects.get(name = 'Self Donation')
	found_participant = Participant.objects.get(fname = 'Scott', lname = 'Welch')
	new_event_record = Participant_Event_Record(guests = 0, event = event, participant = found_participant, hokie_passport_id = 0)
	new_event_record.save()