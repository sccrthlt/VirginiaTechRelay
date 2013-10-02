
#import -datetime
from relayapp.models import *
from django.db.models import Sum
from django.db.models import Count
from django.forms.models import model_to_dict
from operator import itemgetter

class RelayFunctions:

	def participants_unsigned(self, participant):
		candles = {}
		candles['id'] = int(participant)
		candles['fname'] = model_to_dict(Participant.objects.get(pk = participant))['fname']
		candles['lname'] = model_to_dict(Participant.objects.get(pk = participant))['lname']
		
		return candles
	
	def teams_all(self, team):
		candles = {}
		candles['id'] = int(team)
		candles['name'] = model_to_dict(Team.objects.get(pk = team))['name']
		
		return candles

	def participants_milestone_candles(self, team):
		candles = Participant_Milestone_Record.objects.filter(participant__team = team).aggregate(candles_rewarded = Sum('donation_milestone__candles_rewarded'))
		return candles['candles_rewarded'] if candles['candles_rewarded'] is not None else 0

	def participants_emails_candles(self, team):
		participants = Participant.objects.filter(team = team)

		total = 0
		for participant in participants:
			if not participant.fname == 'William' and not participant.lname == 'Castelvecchi' and not participant.fname == 'Christopher' and not participant.lname == 'Millehan':
				for rule in Email_Rule.objects.all():
					if rule.emails <= participant.emails_sent:
						total += participant.emails_sent * rule.candles_rewarded

		return total

		#original call, keep in case we revert
		#candles = Participant_Email_Record.objects.filter(participant__team = team).aggregate(candles_rewarded = Sum('email_milestone__candles_rewarded'))
		#return candles['candles_rewarded'] if candles['candles_rewarded'] is not None else 0

	def participants_event_candles(self, team):

		candles = Participant_Event_Record.objects.filter(participant__team = team).aggregate(candles_rewarded = Sum('event__candles_rewarded'))
		return candles['candles_rewarded'] if candles['candles_rewarded'] is not None else 0

	def participant_specific_info(self, participant):
		tempInfo = {}
		participantObject = Participant.objects.get(pk = participant)
		tempInfo['fname'] = participantObject.fname
		tempInfo['lname'] = participantObject.lname
		tempInfo['team_name'] = str(participantObject.team)
		tempInfo['team_id'] = participantObject.team.id
		tempInfo['id'] = participantObject.id

		return tempInfo

	def participant_specific_totals(self, participant):

		total = {}
		donations_total = Donation.objects.filter(participant = participant).aggregate(total_donations = Sum('amount'))
		total['donations_total'] = float(str(donations_total['total_donations'] if donations_total['total_donations'] is not None else 0))
		total_milestone = Participant_Milestone_Record.objects.filter(participant = participant).aggregate(candles_rewarded = Sum('donation_milestone__candles_rewarded'))
		total['milestone_total'] = float(str(total_milestone['candles_rewarded'] if total_milestone['candles_rewarded'] is not None else 0))

		totalCandles = 0
		total_emails_sent = 0
		participant = Participant.objects.get(pk = participant)
		for rule in Email_Rule.objects.all():
				if rule.emails <= participant.emails_sent:
					totalCandles += participant.emails_sent * rule.candles_rewarded
					total_emails_sent = participant.emails_sent

		total['emails_sent'] = total_emails_sent
		total['emails_candles'] = totalCandles

		eventTotal = 0
		currEventTotal = 0
		events = Participant_Event_Record.objects.filter(participant = participant)
		for event in events:
			eventTotal = currEventTotal + 1

		total['event_total'] = eventTotal
		candles_event = Participant_Event_Record.objects.filter(participant = participant).aggregate(candles_rewarded = Sum('event__candles_rewarded'))
		total['event_candles'] = float(str(candles_event['candles_rewarded'] if candles_event['candles_rewarded'] is not None else 0))
		#total['candles'] = totalCandles + candles_event['candles_rewarded'] + total_milestone['candles_rewarded']

		return total

	def participant_specific_donations(self, participant):
		donation_objects = Donation.objects.filter(participant = participant)

		donations = []
		for donation in donation_objects:
			tempDonation = {}
			tempDonation['datetime'] = donation.datetime.strftime("%m/%d/%y")
			tempDonation['amount'] = float(str(model_to_dict(donation)['amount']))
			donations.append(tempDonation)

		newlist = sorted(donations, key=itemgetter('datetime'), reverse = True)
		return newlist

	def participant_specific_milestones(self, participant):
		milestone_record_objects = Participant_Milestone_Record.objects.filter(participant = participant)

		milestoneRecords = []
		for milestone_record in milestone_record_objects:
			tempMilestoneRecord = {}
			tempMilestoneRecord['date'] = milestone_record.date.strftime("%m/%d/%y")
			tempMilestoneRecord['amount'] = float(str(milestone_record.donation_milestone.donation_amount))
			tempMilestoneRecord['candles'] = milestone_record.donation_milestone.candles_rewarded
			milestoneRecords.append(tempMilestoneRecord)

		newlist = sorted(milestoneRecords, key=itemgetter('amount'), reverse = False)
		return newlist

	def participant_specific_events(self, participant):
		event_record_objects = Participant_Event_Record.objects.filter(participant = participant)

		eventRecords = []
		for event_record in event_record_objects:
			tempEventRecord = {}
			tempEventRecord['date'] = event_record.event.date.strftime("%m/%d/%y")
			tempEventRecord['candles'] = event_record.event.candles_rewarded
			tempEventRecord['name'] = event_record.event.name
			tempEventRecord['description'] = event_record.event.description
			eventRecords.append(tempEventRecord)

		return eventRecords

	def participant_specific_emails(self, participant):
		email_record_objects = Participant_Email_Record.objects.filter(participant = participant)

		emailRecords = []
		for email_record in email_record_objects:
			tempEmailRecord = {}
			tempEmailRecord['date'] = email_record.date.strftime("%d/%m/%y")
			tempEmailRecord['candles'] = email_record.email_milestone.candles_rewarded
			tempEmailRecord['emails'] = email_record.email_milestone.emails
			emailRecords.append(tempEmailRecord)

		return emailRecords




	def participant_specific_info_greek(self, participant):
		tempInfo = {}
		participantObject = Participant.objects.get(pk = participant)
		teamObject = Team.objects.get(pk = participantObject.team.id)
		companyObject = Company.objects.get(pk = teamObject.company.id)
		tempInfo['id'] = participantObject.id
		tempInfo['fname'] = participantObject.fname
		tempInfo['lname'] = participantObject.lname
		tempInfo['team_name'] = str(participantObject.team)
		tempInfo['team_id'] = teamObject.id
		tempInfo['company_name'] = companyObject.name
		tempInfo['company_id'] = companyObject.id

		return tempInfo

	def participant_specific_totals_greek(self, participant):

		total = {}
		donations_total = Donation.objects.filter(participant = participant).aggregate(total_donations = Sum('amount'))
		total['donations_total'] = float(str(donations_total['total_donations'] if donations_total['total_donations'] is not None else 0))

		tshirtTotal = 0
		currTshirtTotal = 0
		tshirts = Participant_TShirt_Purchase_Record.objects.filter(participant = participant)
		for tshirt in tshirts:
			tshirtTotal = currTshirtTotal + 1

		total['tshirt_total'] = tshirtTotal


		eventTotal = 0
		currEventTotal = 0
		events = Participant_Event_Record.objects.filter(participant = participant)
		for event in events:
			eventTotal = currEventTotal + 1

		total['event_total'] = eventTotal
		candles_event = Participant_Event_Record.objects.filter(participant = participant).aggregate(candles_rewarded = Sum('event__candles_rewarded'))
		total['event_candles'] = float(str(candles_event['candles_rewarded'] if candles_event['candles_rewarded'] is not None else 0))

		return total

	def participant_specific_donations_greek(self, participant):
		donation_objects = Donation.objects.filter(participant = participant)

		donations = []
		for donation in donation_objects:
			tempDonation = {}
			tempDonation['datetime'] = donation.datetime.strftime("%d/%m/%y")
			tempDonation['amount'] = float(str(model_to_dict(donation)['amount']))
			donations.append(tempDonation)

		return donations

	def participant_specific_events_greek(self, participant):
		event_record_objects = Participant_Event_Record.objects.filter(participant = participant)

		eventRecords = []
		for event_record in event_record_objects:
			tempEventRecord = {}
			tempEventRecord['date'] = event_record.event.date.strftime("%d/%m/%y")
			tempEventRecord['candles'] = event_record.event.candles_rewarded
			tempEventRecord['name'] = event_record.event.name
			tempEventRecord['description'] = event_record.event.description
			eventRecords.append(tempEventRecord)

		return eventRecords

	def participant_specific_tshirt_greek(self, participant):
		tshirt_record_objects = Participant_TShirt_Purchase_Record.objects.filter(participant = participant)

		tshirtRecords = []
		for tshirt_record in tshirt_record_objects:
			tempTshirtRecord = {}
			tempTshirtRecord['date'] = tshirt_record.date.strftime("%d/%m/%y")
			tempTshirtRecord['candles'] = tshirt_record.tshirt.candles_rewarded
			tempTshirtRecord['name'] = tshirt_record.name
			tempTshirtRecord['quantity'] = tshirt_record.quantity
			eventRecords.append(tempTshirtRecord)

		return tshirtRecords



	def participants_specific_milestone_candles(self, participant):
		candles = Participant_Milestone_Record.objects.filter(participant = participant).aggregate(candles_rewarded = Sum('donation_milestone__candles_rewarded'))
		return candles['candles_rewarded'] if candles['candles_rewarded'] is not None else 0

	def participants_specific_emails_candles(self, participant):
		participant = Participant.objects.get(pk = participant)

		total = 0
		for rule in Email_Rule.objects.all():
			if rule.emails <= participant.emails_sent:
				total += participant.emails_sent * rule.candles_rewarded

		return total





		#candles = Participant_Email_Record.objects.filter(participant = participant).aggregate(candles_rewarded = Sum('email_milestone__candles_rewarded'))
		#return candles['candles_rewarded'] if candles['candles_rewarded'] is not None else 0

	def participants_specific_event_candles(self, participant):
		candles = Participant_Event_Record.objects.filter(participant = participant).aggregate(candles_rewarded = Sum('event__candles_rewarded'))
		return candles['candles_rewarded'] if candles['candles_rewarded'] is not None else 0

	def number_participants_in_company_signed_up(self, company):
		participants = Team.objects.filter(company = company, signup = True).aggregate(participant_count = Count('participant'))
		return participants['participant_count']

	def percentage_of_participants_in_company_signed_up(self, company):
		percentage = (self.number_participants_in_company_signed_up(company) / Company.objects.get(pk = company).total_people_in_chapter) * 100
		return percentage


		#THIS HAS NOT BEEN TESTED YET, BUT IT IS SETUP
	def company_registration_candles(self, company):

				companyObject = Company.objects.get(pk=company)

				candlesTotal = 0

				if companyObject.total_people_in_chapter == 0:
						return 0

				for rule in Company_Registration_Rule:
						participants = Participant.objects.filter(team__company = company).filter(reg_date__lt = rule.date_cutoff)
						if (participants.count() / companyObject.total_people_in_chapter) * 100 > rule.percent_registered:
							candlesTotal += rule.candles_rewarded

				return candlesTotal

	def company_donations(self, company):
		donations = {}
		donations['company_id'] = int(company)
		donations['company_name'] = model_to_dict(Company.objects.get(pk = company))['name']
		donations['company_type'] = model_to_dict(Company.objects.get(pk = company))['company_type']
		company_donations = Donation.objects.filter(participant__team__company = company).aggregate(total_donations = Sum('amount'))
		donations['company_donations'] = float(str(company_donations['total_donations'] if company_donations['total_donations'] is not None else 0))
		return donations


	def team_specific_general_candles(self, participant):
		candles = {}
		candles['participant_id'] = int(participant)
		candles['participant_first_name'] = model_to_dict(Participant.objects.get(pk = participant))['fname']
		candles['participant_last_name'] = model_to_dict(Participant.objects.get(pk = participant))['lname']
		candles['participant_candles_total'] = self.participants_specific_milestone_candles(participant) + self.participants_specific_emails_candles(participant) + self.participants_specific_event_candles(participant)
		candles['participant_donation_milestone_candles'] = self.participants_specific_milestone_candles(participant)
		candles['participant_email_milestone_candles'] = self.participants_specific_emails_candles(participant)
		candles['participant_event_milestone_candles'] = self.participants_specific_event_candles(participant)
		return candles

	def team_specific_general_participants(self, participant):
		candles = {}
		candles['participant_id'] = int(participant)
		candles['participant_first_name'] = model_to_dict(Participant.objects.get(pk = participant))['fname']
		candles['participant_last_name'] = model_to_dict(Participant.objects.get(pk = participant))['lname']
		return candles

	def team_specific_greek_candles(self, participant):
		candles = {}
		candles['participant_id'] = int(participant)
		candles['participant_first_name'] = model_to_dict(Participant.objects.get(pk = participant))['fname']
		candles['participant_last_name'] = model_to_dict(Participant.objects.get(pk = participant))['lname']
		candles['participant_candles_total'] = str('N/A')
		candles['participant_event_milestone_candles'] = self.participants_specific_event_candles(participant)
		candles['participant_tshirt_milestone_candles'] = str('N/A')
		candles['participant_registration_milestone_candles'] = str('N/A')

		donations_total = Donation.objects.filter(participant = participant).aggregate(total_donations = Sum('amount'))
		candles['participant_donations_total'] = float(str(donations_total['total_donations'] if donations_total['total_donations'] is not None else 0))
		return candles

	def company_specific_greek_candles(self, team):
		candles = {}
		candles['team_id'] = int(team)
		candles['team_name'] = model_to_dict(Team.objects.get(pk = team))['name']

		teamObject = Team.objects.get(pk = team)
		candles['company_name'] = teamObject.company.name
		candles['company_id'] = teamObject.company.id
		candles['team_candles_total'] = str('N/A')
		candles['team_event_milestone_candles'] = self.participants_event_candles(team)
		candles['team_tshirt_milestone_candles'] = str('N/A')
		candles['team_registration_milestone_candles'] = ('N/A')

		donations_total = Donation.objects.filter(participant__team = team).aggregate(total_donations = Sum('amount'))
		candles['team_donations_total'] = float(str(donations_total['total_donations'] if donations_total['total_donations'] is not None else 0))
		return candles

	def company_corps_candles(self, company):
		candles = {}
		candles['company_id'] = int(company)
		candles['company_name'] = model_to_dict(Company.objects.get(pk = company))['name']
		candles['company_type'] = model_to_dict(Company.objects.get(pk = company))['company_type']
		candles['company_candles_total'] = self.company_event_candles(company) + self.company_emails_candles(company) + self.company_milestone_candles(company)
		candles['company_donation_milestone_candles'] = self.company_milestone_candles(company)
		candles['company_email_milestone_candles'] = self.company_emails_candles(company)
		candles['company_event_milestone_candles'] = self.company_event_candles(company)

		return candles

	def candles_total(self, company):
		candles=self.company_event_candles(company) + self.company_emails_candles(company) + self.company_milestone_candles(company) + self.company_tshirt_milestone_candles(company) + self.company_registration_candles(company)

		return candles

	def company_greek_candles(self, company):
		candles = {}
		candles['company_id'] = int(company)
		candles['company_name'] = model_to_dict(Company.objects.get(pk = company))['name']
		candles['company_type'] = model_to_dict(Company.objects.get(pk = company))['company_type']
		candles['company_candles_total'] = self.company_registration_candles(company) + self.company_tshirt_milestone_candles(company) + self.company_event_candles(company)
		candles['company_registration_candles'] = self.company_registration_candles(company)
		candles['company_tshirt_candles'] = self.company_tshirt_milestone_candles(company)
		candles['company_event_candles'] = self.company_event_candles(company)


		donations_total = Donation.objects.filter(participant__team__company = company).aggregate(total_donations = Sum('amount'))
		candles['company_donations_total'] = float(str(donations_total['total_donations'] if donations_total['total_donations'] is not None else 0))
		return candles


	def company_corps_candles(self, company):
		candles = {}
		candles['company_id'] = int(company)
		candles['company_name'] = model_to_dict(Company.objects.get(pk = company))['name']
		candles['company_type'] = model_to_dict(Company.objects.get(pk = company))['company_type']
		candles['company_candles_total'] = self.company_event_candles(company) + self.company_emails_candles(company) + self.company_milestone_candles(company)
		candles['company_donation_milestone_candles'] = self.company_milestone_candles(company)
		candles['company_email_milestone_candles'] = self.company_emails_candles(company)
		candles['company_event_milestone_candles'] = self.company_event_candles(company)

		return candles

	def company_milestone_candles(self, company):
		candles = Participant_Milestone_Record.objects.filter(participant__team__company = company).aggregate(candles_rewarded = Sum('donation_milestone__candles_rewarded'))
		return candles['candles_rewarded'] if candles['candles_rewarded'] is not None else 0

	def company_emails_candles(self, company):
		candles = Participant_Email_Record.objects.filter(participant__team__company = company).aggregate(candles_rewarded = Sum('email_milestone__candles_rewarded'))
		return candles['candles_rewarded'] if candles['candles_rewarded'] is not None else 0

	def company_event_candles(self, company):
		candles = Participant_Event_Record.objects.filter(participant__team__company = company).aggregate(candles_rewarded = Sum('event__candles_rewarded'))
		return candles['candles_rewarded'] if candles['candles_rewarded'] is not None else 0

	def company_tshirt_milestone_candles(self, company):
		candles = Company_TShirt_Milestone_Record.objects.filter(company = company).aggregate(candles_rewarded = Sum('tshirt_milestone__candles_rewarded'))
		return candles['candles_rewarded'] if candles['candles_rewarded'] is not None else 0

	def company_registration_candles(self, company):
		candles = Company_Registration_Record.objects.filter(company = company).aggregate(candles_rewarded = Sum('registration_milestone__candles_rewarded'))
		return candles['candles_rewarded'] if candles['candles_rewarded'] is not None else 0
	

	def team_candles(self, team):
		candles = {}
		candles['team_id'] = int(team)
		candles['team_name'] = model_to_dict(Team.objects.get(pk = team))['name']
		candles['team_signup'] = model_to_dict(Team.objects.get(pk = team))['signup']
		candles['team_type'] = model_to_dict(Company.objects.get(team__pk = team))['company_type']
		candles['team_candles_total'] = self.participants_milestone_candles(team) + self.participants_emails_candles(team) + self.participants_event_candles(team)
		candles['team_donation_milestone_candles'] = self.participants_milestone_candles(team)
		candles['team_email_milestone_candles'] = self.participants_emails_candles(team)
		candles['team_event_milestone_candles'] = self.participants_event_candles(team)
		return candles

	def pledge_amount_team(self, team):
		pledge_total = 0
		for participant in Participant.objects.filter(team = team):
			participant_id = participant.pk
			try:
				for pledge in Pledge.objects.filter(participant = participant_id):
					pledge_amount = pledge.pledge_amount
					pledge_total = pledge_total + pledge_amount
			except Pledge.DoesNotExist:
				print('Pledge does not exist')
				
		return str(pledge_total if pledge_total is not None else 0)
	
	def max_pledge_amount_team(self, team):
		max_pledge = 0
		for participant in Participant.objects.filter(team = team):
			participant_id = participant.pk
			try:
				for pledge in Pledge.objects.filter(participant = participant_id):
					curr_max_pledge = pledge.max_pledge_amount
					if curr_max_pledge >= max_pledge:
						max_pledge = curr_max_pledge
			except Pledge.DoesNotExist:
				print('Pledge does not exist')
					
		return str(max_pledge if max_pledge is not None else 0)
			
	def counterTeam(self, team):
		di = {}
		di['pledge_amount'] = self.pledge_amount_team(team)
		di['max_pledge_amount'] = self.max_pledge_amount_team(team)
		
		return di
		
	def pledge_amount_participant(self, id):
		pledge_total = 0
		try:
			for pledge in Pledge.objects.filter(participant = id):
				pledge_amount = pledge.pledge_amount
				pledge_total = pledge_total + pledge_amount
		except Pledge.DoesNotExist:
			print('Pledge does not exist')
				
		return str(pledge_total if pledge_total is not None else 0)
	
	def max_pledge_amount_participant(self, id):
		max_pledge = 0
		try:
			for pledge in Pledge.objects.filter(participant = id):
				curr_max_pledge = pledge.max_pledge_amount
				if curr_max_pledge >= max_pledge:
					max_pledge = curr_max_pledge
		except Pledge.DoesNotExist:
			print('Pledge does not exist')
					
		return str(max_pledge if max_pledge is not None else 0)

	def counterParticipant(self, id):
		di = {}
		fname = Participant.objects.get(pk = id).fname
		lname = Participant.objects.get(pk = id).lname
		di['name'] = fname + ' ' + lname
		di['pledge_amount'] = self.pledge_amount_participant(id)
		di['max_pledge_amount'] = self.max_pledge_amount_participant(id)
		
		return di
