import csv
import os
import sys
import cStringIO
import StringIO
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
import codecs






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
        #csv_file_location = args[0]
        files = glob.glob('/home/vtrelayc/projects/VirginiaTechRelay/relay/public/counter/*')
        print 'oldest:', get_oldest_file(files)
        parseCSVCounter(get_youngest_file(files))
        #change()

		

def get_oldest_file(files, _invert=False):
    """ Find and return the oldest file of input file names.
    Only one wins tie. Values based on time distance from present.
    Use of `_invert` inverts logic to make this a youngest routine,
    to be used more clearly via `get_youngest_file`.
    """
    gt = operator.lt if _invert else operator.gt
    # Check for empty list.
    if not files:
        return None
    # Raw epoch distance.
    now = time.time()
    # Select first as arbitrary sentinel file, storing name and age.
    oldest = files[0], now - os.path.getctime(files[0])
    # Iterate over all remaining files.
    for f in files[1:]:
        age = now - os.path.getctime(f)
        if gt(age, oldest[1]):
            # Set new oldest.
            oldest = f, age
    # Return just the name of oldest file.
    return oldest[0]
	
def get_youngest_file(files):
    return get_oldest_file(files, _invert=True)

def counter(info, noCol):
	helper = RelayFunctions()
	
	try:
		counter = Counter.objects.get(strip_id = info[0])
		team_id = counter.team.pk
		counter_pledge_numbers = helper.counterTeam(team_id)
		pledge_amount = counter_pledge_numbers['pledge_amount']
		max_pledge_amount = counter_pledge_numbers['max_pledge_amount']
		laps_completed = int(noCol)
		
		counter.pledge_amount = pledge_amount
		counter.max_pledge_amount = max_pledge_amount
		counter.laps_completed = laps_completed
		total = laps_completed*pledge_amount
		counter.total = total
		counter.save()
	except Counter.DoesNotExist:
		print('Uh oh')

def change():
	for counter in Counter.objects.all():
		counter.laps_completed = int(0)
		counter.save()

def parseCSVCounter(csv_file):

	#paramFile = open(csv_file).read()
    #portfolio = csv.DictReader(paramFile)
    #data = open(csv_file).read()
    #relayreader = csv.DictReader(cStringIO.StringIO(paramFile), delimiter=',')
    
    with codecs.open(csv_file, "r", "utf-8-sig","strict", -1) as f:
        relayreader = csv.reader(f, delimiter=',')
        for row in relayreader:
            print(row)

            try:
                #row[0] = unicode(row[0], 'latin-1')
                noCol = 0
                for col in row:
                    noCol = noCol + 1
                noCol = noCol - 2
                print(noCol)
                counter(row, noCol)
                print('starting row..')

            except UnicodeDecodeError, e:
                print('something went wrong1')
                print e

            except Exception, e:
                print('something went wrong')
                print e