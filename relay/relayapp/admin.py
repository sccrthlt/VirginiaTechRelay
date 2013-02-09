#relay/relayapp
from django.contrib import admin
from relayapp.models import *

class ParticipantAdmin(admin.ModelAdmin):
	list_display = ('lname', 'fname', 'email', 'team', 'emails_sent')
	search_fields = ['email']
	
class EventAdmin(admin.ModelAdmin):
	list_display = ('name', 'date')
	list_filter = ['date']
	search_fields = ['name']

class DonationAdmin(admin.ModelAdmin):
	list_display = ('participant', 'amount', 'date')
	list_filter = ['date']
	search_fields = ['participant']

class ParticipantMilestoneRecordAdmin(admin.ModelAdmin):
	list_display = ('participant', 'donation_milestone', 'date')
	list_filter = ['date']
	search_fields = ['participant']

class ParticipantEmailRecordAdmin(admin.ModelAdmin):
	list_display = ('participant', 'email_milestone', 'date')
	list_filter = ['date']
	search_fields = ['participant']

class EmailRuleAdmin(admin.ModelAdmin):
	list_display = ('candles_rewarded', 'emails')

admin.site.register(Company)
admin.site.register(Team)
admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(TShirt)
admin.site.register(Donation, DonationAdmin)
admin.site.register(Company_TShirt_Milestone)
admin.site.register(Donation_Milestone)
admin.site.register(Company_Registration_Rule)
admin.site.register(Email_Rule, EmailRuleAdmin)
admin.site.register(Participant_Email_Record, ParticipantEmailRecordAdmin)
admin.site.register(Participant_Event_Record)
admin.site.register(Company_TShirt_Milestone_Record)
admin.site.register(Team_Event_Record)
admin.site.register(Participant_Milestone_Record, ParticipantMilestoneRecordAdmin)
admin.site.register(Participant_TShirt_Purchase_Record)
admin.site.register(Company_Registration_Record)
