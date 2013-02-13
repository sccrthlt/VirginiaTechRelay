import datetime
from relayapp.models import *
from django.db.models import Sum
from django.db.models import Count
from django.forms.models import model_to_dict

class RelayFunctions:

	def participants_milestone_candles(self, team):
		candles = Participant_Milestone_Record.objects.filter(participant__team = team).aggregate(candles_rewarded = Sum('donation_milestone__candles_rewarded'))
		return candles['candles_rewarded'] if candles['candles_rewarded'] is not None else 0

	def participants_emails_candles(self, team):
		participants = Participant.objects.filter(team = team)

		total = 0
		for participant in participants:
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

	def participant_specific_donations(self, participant):
		donation_objects = Donation.objects.filter(participant = participant)

		donations = []
		currDonations = 0
		for donation in donation_objects:
			tempDonation = {}
			tempDonation['date'] = donation.date.strftime("%d/%m/%y")
			tempDonation['amount'] = float(str(model_to_dict(donation)['amount']))

			#not positive if this is what was intended
			tempDonation['total'] = currDonations + float(str(model_to_dict(donation)['amount']))
			
			donations.append(tempDonation)

		return donations

	def participant_specific_milestones(self, participant):
		milestone_record_objects = Participant_Milestone_Record.objects.filter(participant = participant)

		milestoneRecords = []
		currCandles = 0
		for milestone_record in milestone_record_objects:
			tempMilestoneRecord = {}
			tempMilestoneRecord['date'] = milestone_record.date.strftime("%d/%m/%y")
			tempMilestoneRecord['amount'] = float(str(milestone_record.donation_milestone.donation_amount))
			tempMilestoneRecord['candles'] = milestone_record.donation_milestone.candles_rewarded
			
			#not positive if this is what was intended
			tempMilestoneRecord['total'] = currCandles + milestone_record.donation_milestone.candles_rewarded
			
			milestoneRecords.append(tempMilestoneRecord)

		return milestoneRecords

	def participant_specific_events(self, participant):
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

	def participants_specific_milestone_candles(self, participant):
		candles = Participant_Milestone_Record.objects.filter(participant = participant).aggregate(candles_rewarded = Sum('donation_milestone__candles_rewarded'))
		return candles['candles_rewarded'] if candles['candles_rewarded'] is not None else 0

	def participants_specific_emails_candles(self, participant):
		candles = Participant_Email_Record.objects.filter(participant = participant).aggregate(candles_rewarded = Sum('email_milestone__candles_rewarded'))
		return candles['candles_rewarded'] if candles['candles_rewarded'] is not None else 0

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

	def company_candles(self, company):
		candles = {}
		candles['company_id'] = int(company)
		candles['company_name'] = model_to_dict(Company.objects.get(pk = company))['name']
		candles['company_type'] = model_to_dict(Company.objects.get(pk = company))['company_type']
		candles['company_candles_total'] = self.company_event_candles(company) + self.company_tshirt_milestone_candles(company) + self.company_registration_candles(company)
		candles['company_event_milestone_candles'] = self.company_event_candles(company)
		candles['company_tshirt_milestone_candles'] = self.company_tshirt_milestone_candles(company)
		candles['company_registration_milestone_candles'] = self.company_registration_candles(company)

		company_donations = Donation.objects.filter(participant__team__company = company).aggregate(total_donations = Sum('amount'))
		candles['company_donations_total'] = float(str(company_donations['total_donations'] if company_donations['total_donations'] is not None else 0))

		return candles


	def participant_specific_general_candles(self, participant):
		candles = {}
		candles['participant_id'] = int(participant)
		#candles['participant_email'] = model_to_dict(Participant.objects.get(pk = participant))['email']
		candles['participant_first_name'] = model_to_dict(Participant.objects.get(pk = participant))['fname']
		candles['participant_last_name'] = model_to_dict(Participant.objects.get(pk = participant))['lname']
		candles['participant_candles_total'] = self.participants_specific_milestone_candles(participant) + self.participants_specific_emails_candles(participant) + self.participants_specific_event_candles(participant)
		candles['participant_donation_milestone_candles'] = self.participants_specific_milestone_candles(participant)
		candles['participant_email_milestone_candles'] = self.participants_specific_emails_candles(participant)
		candles['participant_event_milestone_candles'] = self.participants_specific_event_candles(participant)
		return candles

	def candles_total(self, team):
		candles=self.company_event_candles(company) + self.company_emails_candles(company) + self.company_milestone_candles(company) + self.company_tshirt_milestone_candles(company) + self.company_registration_candles(company) + self.company_donation_milestone_candles(company) + self.participants_milestone_candles(team) + self.participants_emails_candles(team) + self.participants_event_candles(team)

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

	def company_donation_milestone_candles(self, company):
		candles = Participant_Milestone_Record.objects.filter(participant__team__company = company).aggregate(candles_rewarded = Sum('donation_milestone__candles_rewarded'))
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
