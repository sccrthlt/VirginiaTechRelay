from django.core.management.base import BaseCommand, CommandError
import csv
import os
import cStringIO
from datetime import datetime, date, time
import datetime
from relayapp.models import *

class Command(BaseCommand):
    args = 'CSV file with <Team> detail data'
    help = 'Parses CSV files related to team fundraising'

    def handle(self, *args, **options):
        print "Starting Command.."
        csv_file_location = args[0]
        print sys.getdefaultencoding()
        # parseCSVTeamFundraising(csv_file_location)

def setupCompany(info):

    try:
        c = Company.objects.get(name='General Company')
    except Company.DoesNotExist:
        c = Company(name='General Company')
        c.save()
    finally:
        company_return = c

    if (info['Public Company Name'] != 'N/A'):
        try:
            company_check = Company.objects.get(name = info['Public Company Name'])
        except Company.DoesNotExist:
            company_check = Company(name = info['Public Company Name'], company_type = 'RT')
            company_check.save()

        company_return = company_check

    return company_return

def getCompany(info):

    company_return = Company.objects.get(name = 'General Company')

    if (info['Public Company Name'] != 'N/A'):
        company_return = Company.objects.get(name = info['Public Company Name'])

    return company_return

def setupTeam(info):
    # print('team: ' + info['Team Name'])

    try:
        team_return = Team.objects.get(name = info['Team Name'])
    except Team.DoesNotExist:
        team_company = getCompany(info)
        team_return = Team(name = info['Team Name'], company = team_company, signup = False)
        team_return.save()

    return team_return

def setupCaptain(info):

    try:
        cap_return = Participant.objects.get(email = info['Team Captain Email Address'])
    except Participant.DoesNotExist:
        cap_return = Participant(
            fname = info['Team Captain First Name'],
            lname = info['Team Captain Last Name'],
            email = info['Team Captain Email Address'],
            team = Team.objects.get(name = info['Team Name']),
            reg_date = datetime.date.today()
        )
        cap_return.save()

    return cap_return

def parseCSVTeamFundraising(csv_file_location):

    data = open(csv_file_location).read()
    relayreader = csv.DictReader(cStringIO.StringIO(data), delimiter=',')

    for row in relayreader:

        try:
            row['Team Name'].decode('ascii')

            company = setupCompany(row)
            team = setupTeam(row)
            captain = setupCaptain(row)

            company.captain = captain
            company.save()

        except UnicodeDecodeError, e:
            print row
            print e

            # print ("it was not a ascii-encoded unicode string")
        # else:
            # print ("It may have been an ascii-encoded unicode string")

        # print (row)
        # print ('\n')

