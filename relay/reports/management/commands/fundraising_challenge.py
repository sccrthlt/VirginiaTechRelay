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
		createFundraisingChallengeStartRecord()

def createFundraisingChallengeStartRecord()
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
					print('Record DNE.  Creating start record...')
					try:
						new_fundraising_challenge_start_record = Fundraising_Challenge_Start_Record(
                            participant = participant,
                            challenge = challenge,
                            amount_raised = total_donations,
                            candles_raised = total_candles,
                            datetime_start = challenge.datetime_start,
                            )
		except:
			print('No challenges')

	createFundraisingChallengeRecord()
			
def createFundraisingChallengeRecord():
	helper = RelayFunctions()
	
	
	for challenge in Fundraising_Challenge.objects.all():
		if  challenge.datetime_start <= datetime.datetime.now() <= challenge.datetime_end:
			if not challenge.amount_raised == 0 and challenge.candles_raised == 0:
				for participant in Participant.objects.all():
					currentRaised = Donation.objects.filter(participant = participant).aggregate(total_donations = Sum('amount'))
					startRaised = Fundraising_Challenge_Start_Record.objects.filter(participant = participant).amount_raised
					try:
						record = Fundraising_Challenge_Record.objects.get(participant = participant, challenge = challenge)
						Fundraising_Challenge_Record.objects.get(participant = participant, challenge = challenge).delete()
						if currentRaised > startRaised:
							save_participant = Participant.objects.get(pk = participant)
							donated_datetime = Donation.objects.filter(participant = participant).annotate(most_recent_donation_datetime = Max('datetime'))
							new_fundraising_record = Fundraising_Challenge_Record(participant = save_participant, challenge = challenge, datetime = donated_datetime[0].most_recent_donation_datetime)
							new_fundraising_record.save()
					except Fundraising_Challenge_Record.DoesNotExist:
						print('Fundraising_Challenge_Record does not exist')
			if not challenge.candles_raised == 0 and challenge.amount_raised == 0:
				for participant in Participant.objects.all():
					totals = helper.participant_specific_totals(model_to_dict(participant)['id'])
					currentRaised = totals.milestone_total + totals.emails_candles + totals.event_candles
					startRaised = Fundraising_Challenge_Start_Record.objects.filter(participant = participant).candles_raised
					try:
						record = Fundraising_Challenge_Record.objects.filter(participant = participant, challenge = challenge)
						Fundraising_Challenge_Record.objects.get(participant = participant, challenge = challenge).delete()
						if currentRaised > startRaised:
							save_participant = Participant.objects.get(pk = participant)
							donated_datetime = Donation.objects.filter(participant = participant).annotate(most_recent_donation_datetime = Max('datetime'))
							new_fundraising_record = Fundraising_Challenge_Record(participant = save_participant, challenge = challenge, datetime = donated_datetime[0].most_recent_donation_datetime)
							new_fundraising_record.save()
					except Fundraising_Challenge_Record.DoesNotExist:
						print('Fundraising_Challenge_Record does not exist')
			else:
				print('No amount_raised or candles_raised specified')
		else:
			print('No challenge currently running')
	except:
		print('No challenges')