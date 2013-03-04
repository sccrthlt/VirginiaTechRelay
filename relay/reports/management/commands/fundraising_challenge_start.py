from django.core.management.base import BaseCommand, CommandError
import csv
import os
import time
import cStringIO

from django.forms.models import model_to_dict
from django.db.models import Sum
from django.db.models import Max
from datetime import datetime

from relayapp.models import *
from relayapp.RelayFunctions import *

class Command(BaseCommand):
    args = 'CSV file with <Donation> detail data'
    help = 'Parses CSV files related to donation details'

    def handle(self, *args, **options):
        print "Starting Command.."
		setupFundraisingChallengeRecord()

def setupFundraisingChallengeRecord()
	helper = RelayFunctions()
	
	for participant in Participant.objects.all()
		totals = helper.participant_specific_totals(model_to_dict(participant)['id'])
		total_donations = totals.donations_total
		total_candles = totals.milestone_total + totals.emails_candles + totals.event_candles
		try:
			for challenge in Fundraising_Challenge.objects.all()
				try:
					fundraising_challenge_start_record = Fundraising_Challenge_Start_Record(participant = participant, challenge = challenge)
				except Fundraising_Challenge_Start_Record.DoesNotExist:
					try:
						new_fundraising_challenge_start_record = Fundraising_Challenge_Start_Record(
                            participant = participant,
                            challenge = challenge,
                            amount_raised = total_donations,
                            candles_raised = total_candles,
		except:
			print('No challenges')