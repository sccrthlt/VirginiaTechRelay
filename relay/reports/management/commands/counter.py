import csv
import os
import sys
import cStringIO
from datetime import datetime, date, time
import datetime
from relayapp.models import *
from relayapp.RelayFunctions import *
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
import urllib2
from django.core.management.base import BaseCommand, CommandError
import os, glob, time, operator






#@csrf_exempt
#def upload_file(request):

	#if request.method == 'POST':
		#csv_file = request.FILES['test']
		#parseCSVCounter(csv_file)
		#return HttpResponse(status=400)
	#else:
		#return HttpResponse(status=400)
	#return render_to_response('base.html', {'form': form})

class Command(BaseCommand):
    args = 'CSV file with <Donation> detail data'
    help = 'Parses CSV files related to donation details'

    def handle(self, *args, **options):
        print "Starting Command.."
        #s = model_to_dict(Participant.objects.get(email = 'scott2@vt.edu'))['id']
        #setupUser()
		csv_file_location = args[0]
        parseCSVCounter(csv_file_location)

	
def counter(info):
	helper = RelayFunctions()
	
	try:
		counter_object = Counter.object.get(strip_id = info[0])
		team_object = counter_object.team
		team_id = team_object.pk
		counter_pledge_numbers = helper.counter(team_id)
		pledge_amount = counter_pledge_numbers.pledge_amount
		max_pledge_amount = counter_pledge_numbers.max_pledge_amount
		laps_completed = info[
	except Counter.DoesNotExist:
		print('Uh oh')

def parseCSVCounter(csv_file):

    paramFile = csv_file.read()
    #portfolio = csv.DictReader(paramFile)
    #data = open(csv_file).read()
    relayreader = csv.DictReader(cStringIO.StringIO(paramFile), delimiter=',')

    for row in relayreader:

        try:
            row[0] = unicode(row[0], 'latin-1')

            counter = counter(row)

        except UnicodeDecodeError, e:
            print e

        except Exception, e:
            print e