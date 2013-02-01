from relayapp.models import *
from django.db.models import Sum
from django.db.models import Count

class RelayFunctions:

    def participants_milestone_candles(self, team):
            return Participant_Milestone_Record.objects.filter(participant__team = team).aggregate(candles_rewarded = Sum('donation_milestone__candles_rewarded'))

    def participants_emails_candles(self, team):
            return Participant_Email_Record.objects.filter(participant__team = team).aggregate(candles_rewarded = Sum('email_milestone__candles_rewarded'))

    def participants_event_candles(self, team):
            return Participant_Event_Record.objects.filter(participant__team = team).aggregate(candles_rewarded = Sum('event__candles_rewarded'))

    def company_tshirt_milestone_candles(self, company):
            return Company_TShirt_Milestone_Record.objects.filter(company = company).aggregate(candles_rewarded = Sum('tshirt_milestone__candles_rewarded'))

    def number_participants_in_company(self, company):
            return Team.objects.filter(company = company).aggregate(participant_count = Count('participant'))                                                                                               
