import csv
import os
import codecs

from relayapp.models import *

def setupCompany(info):

    company_return = Company.objects.get(name = 'General Company')

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

    print('team: ' + info['Team Name'])

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
	cap_return = Participant(fname = info['Team Captain First Name'], lname = info['Team Captain Last Name'], email = info['Team Captain Email Address'], team = Team.objects.get(name = info['Team Name']))
	cap_return.save()

    return cap_return

def parseCSVTeamFundraising():

    #open('TeamFundraising.csv', 'rt')
    #codecs.open('TeamFundraising.csv', 'r', encoding='utf-8')
    with open('TeamFundraising.csv', 'rt') as csvfile:

	relayreader = csv.DictReader(csvfile, delimiter=',')

	for row in relayreader:

	    try:
		row['Team Name'].decode('ascii')

		company = setupCompany(row)
		team = setupTeam(row)
		captain = setupCaptain(row)

		company.captain = captain
		company.save()

	    except UnicodeDecodeError:
		print ("it was not a ascii-encoded unicode string")
	    else:
		print ("It may have been an ascii-encoded unicode string")

	    print (row)
	    print ('\n')
