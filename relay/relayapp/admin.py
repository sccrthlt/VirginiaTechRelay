#relay/relayapp
from django.contrib import admin
from relayapp.models import *

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('lname', 'fname', 'email', 'team', 'emails_sent', 'hokie_passport_id', 'facebook_username')
    search_fields = ['email']

class TeamCaptainAdmin(admin.ModelAdmin):
    list_display = ('lname', 'fname', 'email', 'team', 'reg_date')
    search_fields = ['email']

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'candles_rewarded', 'homepage')
    list_filter = ['date']
    search_fields = ['name']

class FundraisingChallengeAdmin(admin.ModelAdmin):
    list_display = ('name', 'datetime_start', 'datetime_end', 'amount_raised', 'candles_raised', 'candles_rewarded', 'homepage')
    list_filter = ['datetime_start']
    search_fields = ['name']

class FundraisingChallengeRecordAdmin(admin.ModelAdmin):
    list_display = ('participant', 'challenge', 'candles_rewarded', 'datetime')
    list_filter = ['datetime']
    search_fields = ['participant']

class FundraisingChallengeTrackerRecordAdmin(admin.ModelAdmin):
    list_display = ('participant', 'challenge', 'difference_raised', 'difference_candles', 'datetime')
    list_filter = ['datetime']
    search_fields = ['participant']

class FundraisingChallengeStartRecordAdmin(admin.ModelAdmin):
    list_display = ('participant', 'challenge', 'amount_raised', 'candles_raised', 'datetime_start')
    list_filter = ['datetime_start']
    search_fields = ['participant']

class DonationAdmin(admin.ModelAdmin):
    list_display = ('participant', 'amount', 'datetime')
    list_filter = ['datetime']
    search_fields = ['participant']

class ParticipantMilestoneRecordAdmin(admin.ModelAdmin):
    list_display = ('participant', 'donation_milestone', 'datetime')
    list_filter = ['datetime']
    search_fields = ['participant']

class ParticipantEmailRecordAdmin(admin.ModelAdmin):
    list_display = ('participant', 'email_milestone', 'datetime')
    list_filter = ['datetime']
    search_fields = ['participant']

class EmailRuleAdmin(admin.ModelAdmin):
    list_display = ('candles_rewarded', 'emails')

class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'signup')
    list_filter = ['signup']
    search_fields = ['name']

class ParticipantEventRecordAdmin(admin.ModelAdmin):
    list_display = ('participant', 'hokie_passport_id', 'event', 'guests',)
    list_filter = ['event']
    search_fields = ['participant']

class CompanyRegistrationRuleAdmin(admin.ModelAdmin):
    list_display = ('percent_registered', 'date_cutoff', 'candles_rewarded')
    list_filter = ['percent_registered']
    search_fields = ['percent_registered']

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'captain', 'total_people_in_chapter', 'company_type')
    list_filter = ['name']
    search_fields = ['name']

class OlympicsLapCounterSignupAdmin(admin.ModelAdmin):
    list_display = ('team', 'company', 'captain', 'captain_email', 'olympics', 'tier', 'counter', 'datetime')
    list_filter = ['company']
    search_fields = ['team']

class PledgeAdmin(admin.ModelAdmin):
    list_display = ('sponsor', 'participant', 'pledge_amount', 'max_pledge_amount', 'datetime')
    list_filter = ['sponsor']
    search_fields = ['sponsor']

class CounterAdmin(admin.ModelAdmin):
    list_display = ('team', 'strip_id', 'tier', 'pledge_amount', 'max_pledge_amount', 'laps_completed', 'total')
    list_filter = ['team']
    search_fields = ['team']

admin.site.register(Counter, CounterAdmin)
admin.site.register(Pledge, PledgeAdmin)
admin.site.register(Olympics_Lap_Counter_Signup, OlympicsLapCounterSignupAdmin)
admin.site.register(Team_Captain, TeamCaptainAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Event, EventAdmin)
#admin.site.register(TShirt)
admin.site.register(Donation, DonationAdmin)
admin.site.register(Candles_Record)
#admin.site.register(Company_TShirt_Milestone)
admin.site.register(Donation_Milestone)
admin.site.register(Fundraising_Challenge, FundraisingChallengeAdmin)
admin.site.register(Fundraising_Challenge_Record, FundraisingChallengeRecordAdmin)
admin.site.register(Fundraising_Challenge_Tracker_Record, FundraisingChallengeTrackerRecordAdmin)
admin.site.register(Fundraising_Challenge_Start_Record, FundraisingChallengeStartRecordAdmin)
#admin.site.register(Company_Registration_Rule, CompanyRegistrationRuleAdmin)
admin.site.register(Email_Rule, EmailRuleAdmin)
admin.site.register(Participant_Email_Record, ParticipantEmailRecordAdmin)
admin.site.register(Participant_Event_Record, ParticipantEventRecordAdmin)
#admin.site.register(Company_TShirt_Milestone_Record)
admin.site.register(Team_Event_Record)
admin.site.register(Participant_Milestone_Record, ParticipantMilestoneRecordAdmin)
admin.site.register(Participant_TShirt_Purchase_Record)
#admin.site.register(Company_Registration_Record)
