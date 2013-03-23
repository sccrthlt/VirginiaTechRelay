import csv
import os
import sys
import cStringIO
from datetime import datetime, date, time
import datetime
from relayapp.models import *





def parseCSVCounter(csv_file_location):

    data = open(csv_file_location).read()
    relayreader = csv.DictReader(cStringIO.StringIO(data), delimiter=',')

    for row in relayreader:

        try:
            row['Team Name'] = unicode(row['Team Name'], 'latin-1')

            company = setupCompany(row)

        except UnicodeDecodeError, e:
            print e

        except Exception, e:
            print e

    general_team_info = {'Team Name':'General Team', 'Public Company Name':'N/A'}
    setupTeam(general_team_info)
        # else:
        #     print "Unble to save?"

            # print ("it was not a ascii-encoded unicode string")
        # else:
            # print ("It may have been an ascii-encoded unicode string")

        # print (row)
        # print ('\n')