from django.core.management.base import BaseCommand, CommandError
import csv
import os
import time
import cStringIO
import pytz


from django.forms.models import model_to_dict
from django.db.models import Sum
from django.db.models import Max
from datetime import datetime
from django.utils import timezone

from relayapp.models import *
from relayapp.RelayFunctions import *

class Command(BaseCommand):
    args = 'CSV file with <Donation> detail data'
    help = 'Parses CSV files related to donation details'

    def handle(self, *args, **options):
        print "Starting Command.."
        createFundraisingChallengeStartRecord()

def createFundraisingChallengeStartRecord():
	helper = RelayFunctions()
	
	for participant in Participant.objects.all():
		totals = helper.participant_specific_totals(model_to_dict(participant)['id'])
		total_donations = totals['donations_total']
		total_candles = totals['milestone_total'] + totals['emails_candles'] + totals['event_candles']
		try:
			for challenge in Fundraising_Challenge.objects.all():
				try:
					fundraising_challenge_start_record = Fundraising_Challenge_Start_Record(participant = participant, challenge = challenge)
				except Fundraising_Challenge_Start_Record.DoesNotExist:
					print('Record DNE.  Creating start record...')
					new_fundraising_challenge_start_record = Fundraising_Challenge_Start_Record(participant = participant, challenge = challenge, amount_raised = total_donations, candles_raised = total_candles, datetime_start = challenge.datetime_start)
					new_fundraising_challenge_start_record.save()
		except Exception:
			print('No challenges')

	createFundraisingChallengeRecord()
			
def createFundraisingChallengeRecord():
	helper = RelayFunctions()
	timezone.now()
	utc=pytz.UTC
	
	
	
	for challenge in Fundraising_Challenge.objects.all():
		if challenge.datetime_start <= datetime.now(utc) <= challenge.datetime_end:
			if not challenge.amount_raised == 0 and challenge.candles_raised == 0:
				for participant in Participant.objects.all():
					save_participant = Participant.objects.get(pk = participant)
					currentRaised = Donation.objects.filter(participant = participant).aggregate(total_donations = Sum('amount'))
					startRecord = Fundraising_Challenge_Start_Record.objects.get(participant = participant, challenge = challenge)
					startRaised = startRecord.amount_raised
					diffRaised = currentRaised - startRaised
					print('Checking to see if record is deserved')
					if diffRaised > challenge.amount_raised:
						try:
							print('Already created...editing')
							record = Fundraising_Challenge_Record.objects.get(participant = participant, challenge = challenge)
							Fundraising_Challenge_Record.objects.get(participant = participant, challenge = challenge).delete()
							donations = Donation.objects.filter(participant = participant).order_by('datetime')
							tot = 0
							stop = 0
							for donation in donations:
								if stop == 0:
									if tot < challenge.amount_raised:
										amoun = donation.amount
										tot = tot + amoun
									else:
										donated_datetime = donation.datetime
										stop = 1
							#donated_datetime = Donation.objects.filter(participant = participant).annotate(most_recent_donation_datetime = Max('datetime'))
							new_fundraising_record = Fundraising_Challenge_Record(participant = save_participant, challenge = challenge, datetime = donated_datetime, candles_rewarded = challenge.candles_rewarded)
							new_fundraising_record.save()
						except Fundraising_Challenge_Record.DoesNotExist:
							print('Deserved...Fundraising_Challenge_Record does not exist...creating one...')
							donations = Donation.objects.filter(participant = participant).order_by('datetime')
							tot = 0
							stop = 0
							for donation in donations:
								if stop == 0:
									if tot < challenge.amount_raised:
										amoun = donation.amount
										tot = tot + amoun
									else:
										donated_datetime = donation.datetime
										stop = 1
							#donated_datetime = Donation.objects.filter(participant = participant).annotate(most_recent_donation_datetime = Max('datetime'))
							new_fundraising_record = Fundraising_Challenge_Record(participant = save_participant, challenge = challenge, datetime = donated_datetime, candles_rewarded = challenge.candles_rewarded)
							new_fundraising_record.save()
					else:
						print('It is not deserved')
			if not challenge.candles_raised == 0 and challenge.amount_raised == 0:
				for participant in Participant.objects.all():
					totals = helper.participant_specific_totals(model_to_dict(participant)['id'])
					currentCandles = totals['milestone_total'] + totals['emails_candles'] + totals['event_candles']
					startRecord = Fundraising_Challenge_Start_Record.objects.get(participant = participant, challenge = challenge)
					startCandles = startRecord.candles_raised
					diffCandles = currentCandles - startCandles
					if diffCandles > challenge.amount_raised:
						try:
							record = Fundraising_Challenge_Record.objects.filter(participant = participant, challenge = challenge)
							Fundraising_Challenge_Record.objects.get(participant = participant, challenge = challenge).delete()
							save_participant = Participant.objects.get(pk = participant)
							new_fundraising_record = Fundraising_Challenge_Record(participant = save_participant, challenge = challenge, datetime = donated_datetime[0].most_recent_donation_datetime, candles_rewarded = challenge.candles_rewarded)
							new_fundraising_record.save()
						except Fundraising_Challenge_Record.DoesNotExist:
							print('Fundraising_Challenge_Record does not exist')
			else:
				print('No amount_raised or candles_raised specified.  Or both specified at the same time.')
		else:
			print('No challenge currently running')

	createFundraisingChallengeTrackerRecord()

def createFundraisingChallengeTrackerRecord():
	helper = RelayFunctions()
	
	timezone.now()
	utc=pytz.UTC
	
	
	for challenge in Fundraising_Challenge.objects.all():
		if challenge.datetime_start <= datetime.now(utc) <= challenge.datetime_end:
			if not challenge.amount_raised == 0 and challenge.candles_raised == 0:
				for participant in Participant.objects.all():
					currentRaised = Donation.objects.filter(participant = participant).aggregate(total_donations = Sum('amount'))
					startRecord = Fundraising_Challenge_Start_Record.objects.get(participant = participant, challenge = challenge)
					startRaised = startRecord.amount_raised
					diffRaised = currentRaised - startRaised
					try:
						record = Fundraising_Challenge_Tracker_Record.objects.get(participant = participant, challenge = challenge)
						Fundraising_Challenge_Tracker_Record.objects.get(participant = participant, challenge = challenge).delete()
						if not diffRaised == 0:
							save_participant = Participant.objects.get(pk = participant)
							donated_datetime = Donation.objects.filter(participant = participant).annotate(most_recent_donation_datetime = Max('datetime'))
							new_fundraising_record = Fundraising_Challenge_Tracker_Record(participant = save_participant, challenge = challenge, datetime = donated_datetime[0].most_recent_donation_datetime, difference_raised = diffRaised)
							new_fundraising_record.save()
					except Fundraising_Challenge_Tracker_Record.DoesNotExist:
						print('Fundraising_Challenge_Record does not exist')
			if not challenge.candles_raised == 0 and challenge.amount_raised == 0:
				for participant in Participant.objects.all():
					totals = helper.participant_specific_totals(model_to_dict(participant)['id'])
					currentCandles = totals['milestone_total'] + totals['emails_candles'] + totals['event_candles']
					startRecord = Fundraising_Challenge_Start_Record.objects.get(participant = participant, challenge = challenge)
					startCandles = startRecord.candles_raised
					diffCandles = currentCandles - startCandles
					try:
						record = Fundraising_Challenge_Tracker_Record.objects.filter(participant = participant, challenge = challenge)
						Fundraising_Challenge_Tracker_Record.objects.get(participant = participant, challenge = challenge).delete()
						if not diffCandles == 0:
							save_participant = Participant.objects.get(pk = participant)
							donated_datetime = Donation.objects.filter(participant = participant).annotate(most_recent_donation_datetime = Max('datetime'))
							new_fundraising_record = Fundraising_Challenge_Tracker_Record(participant = save_participant, challenge = challenge, datetime = donated_datetime[0].most_recent_donation_datetime, difference_candles = diffCandles)
							new_fundraising_record.save()
					except Fundraising_Challenge_Tracker_Record.DoesNotExist:
						print('Fundraising_Challenge_Record does not exist')
			else:
				print('No amount_raised or candles_raised specified')
		else:
			print('No challenge currently running')