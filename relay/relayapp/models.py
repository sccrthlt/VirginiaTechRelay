#relay/relayapp
from django.db import models
from decimal import Decimal
from django.contrib.auth.models import User

class Company(models.Model):

    RELAY = 'RT'
    GREEK = 'GT'
    CORE = 'CT'

    COMPANY_TYPES = ((RELAY, 'Relay'),(GREEK, 'Greek'),(CORE, 'Core'),)

    name = models.CharField(verbose_name='Company Name', max_length=100)
    captain = models.ForeignKey('Participant', blank=True, null=True)
    total_people_in_chapter = models.PositiveIntegerField(default=0, blank=True)
    company_type = models.CharField(max_length=2, choices=COMPANY_TYPES, default=RELAY)

    #add field for total participants, default to 0, allow blank
    #tshirt milestone can be figured out by using the percentages from the data
    def __unicode__(self):
        return self.name

#move type to company
class Team(models.Model):
    name = models.CharField(verbose_name='Team Name', max_length=100)
    company = models.ForeignKey(Company)
    signup = models.BooleanField()


    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Participant(models.Model):
    fname = models.CharField(verbose_name='First Name', max_length=100)
    lname = models.CharField(verbose_name='Last Name', max_length=100)
    email = models.EmailField(blank=False)
    #milestone can be figured from data
    emails_sent = models.PositiveIntegerField(default=0, blank=True)
    team = models.ForeignKey(Team)
    reg_date = models.DateField()
    hokie_passport_id = models.BigIntegerField(blank=True, default=0)
    facebook_username = models.CharField(max_length=100, default='none')

    #tshirt purchase totals based on records
    #donation totals will be based on donation records with this participant key
    #event totals will be based on the events with this participant key and value of the event

    def __unicode__(self):
        return self.lname + ", " + self.fname

    class Meta:
        ordering = ['lname', 'fname']
	
class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    start_time = models.TimeField(default=None, blank=True, null=True)
    end_time = models.TimeField(default=None, blank=True, null=True)
    candles_rewarded = models.IntegerField()
    prize = models.CharField(max_length=100, default=None, blank=True, null=True)
    description = models.TextField(blank=True)
    image = models.URLField(blank = True)
    homepage = models.BooleanField()

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['date']

class Donation(models.Model):
    participant = models.ForeignKey(Participant)
    amount = models.DecimalField(default=Decimal('0.00'), max_digits=10, decimal_places=2, blank=True)
    datetime = models.DateTimeField()

class Team_Captain(models.Model):
	fname = models.CharField(verbose_name='First Name', max_length=100)
	lname = models.CharField(verbose_name='Last Name', max_length=100)
	email = models.EmailField(blank=False)
	team = models.ForeignKey(Team)
	reg_date = reg_date = models.DateField()





## General Teams System


class Donation_Milestone(models.Model):
    donation_amount = models.DecimalField(default=Decimal('0.00'), max_digits=10, decimal_places=2, blank=True)
    candles_rewarded = models.PositiveIntegerField()

    def __unicode__(self):
        return 'Milestone: ' + str(self.donation_amount) + ' Candles: ' + str(self.candles_rewarded)

    class Meta:
        ordering = ['candles_rewarded']

class Email_Rule(models.Model):
    candles_rewarded = models.PositiveIntegerField()
    emails = models.PositiveIntegerField()

    def __unicode__(self):
        return 'Emails: ' + str(self.emails) + ' Candles: ' + str(self.candles_rewarded)

class Participant_Milestone_Record(models.Model):
    participant = models.ForeignKey(Participant)
    donation_milestone = models.ForeignKey(Donation_Milestone)
    datetime = models.DateTimeField(default = '1993-05-07 12:12')

class Participant_Email_Record(models.Model):
    participant = models.ForeignKey(Participant)
    email_milestone = models.ForeignKey(Email_Rule)
    datetime = models.DateField(default = '1993-05-07 12:12')

class Participant_Event_Record(models.Model):
    guests = models.PositiveIntegerField(default=0, blank=True)
    event = models.ForeignKey(Event)
    participant = models.ForeignKey(Participant)
    hokie_passport_id = models.BigIntegerField(blank=True, default=0)

class Team_Event_Record(models.Model):
    event = models.ForeignKey(Event)
    team = models.ForeignKey(Team)



## Greeks

class TShirt(models.Model):
    name = models.CharField(max_length=200)

class Company_TShirt_Milestone(models.Model):
    percentage_purchased = models.PositiveIntegerField(default=0, blank=True)
    candles_rewarded = models.PositiveIntegerField()

class Company_Registration_Rule(models.Model):
    percent_registered = models.PositiveIntegerField(default=0, blank=True)
    candles_rewarded = models.PositiveIntegerField()
    date_cutoff = models.DateField()

class Company_TShirt_Milestone_Record(models.Model):
    company = models.ForeignKey(Company)
    tshirt_milestone = models.ForeignKey(Company_TShirt_Milestone)
    date = models.DateField()

class Participant_TShirt_Purchase_Record(models.Model):
    participant = models.ForeignKey(Participant)
    tshirt = models.ForeignKey(TShirt)
    quantity = models.PositiveIntegerField(default=0, blank=True)
    date = models.DateField()

class Company_Registration_Record(models.Model):
    company = models.ForeignKey(Company)
    registration_milestone = models.ForeignKey(Company_Registration_Rule)
    date = models.DateField()	
	

##  Candles Record
	
class Candles_Record(models.Model):
	CANDLE_TYPE = (('DO', 'From donation'),('EM', 'From email'),('EV', 'From event'))
	participant = models.ForeignKey(Participant)
	candle_type = models.CharField(max_length=2, choices=CANDLE_TYPE, default='DO')
	candles_value = models.IntegerField(default=0)
	datetime = models.DateTimeField()

	

##  Fundraising Challenge	
	
class Fundraising_Challenge(models.Model):
	name = models.CharField(max_length=100)
	datetime_start = models.DateTimeField()
	datetime_end = models.DateTimeField()
	amount_raised = models.DecimalField(default=Decimal('0.00'), max_digits=10, decimal_places=2, blank=True)
	candles_raised = models.IntegerField(default=0)
	candles_rewarded = models.IntegerField(default=0)
	description = models.TextField(blank=True)
	image = models.URLField(blank = True)
	homepage = models.BooleanField()

class Fundraising_Challenge_Record(models.Model):
	participant = models.ForeignKey(Participant)
	challenge = models.ForeignKey(Fundraising_Challenge)
	candles_rewarded = models.IntegerField(default=0)
	datetime = models.DateTimeField()

class Fundraising_Challenge_Tracker_Record(models.Model):
	participant = models.ForeignKey(Participant)
	challenge = models.ForeignKey(Fundraising_Challenge)
	difference_raised = models.IntegerField(default=0)
	difference_candles = models.IntegerField(default=0)
	datetime = models.DateTimeField()
	
def getDefaultChallenge():
	return Fundraising_Challenge.objects.get(name = 'Cool')
	
class Fundraising_Challenge_Start_Record(models.Model):
	participant = models.ForeignKey(Participant)
	challenge = models.ForeignKey('Fundraising_Challenge', default = getDefaultChallenge)
	amount_raised = models.DecimalField(default=Decimal('0.00'), max_digits=10, decimal_places=2, blank=True)
	candles_raised = models.IntegerField(default=0)
	datetime_start = models.DateTimeField()	
	

## Lap Counter	

class Olympics_Lap_Counter_Signup(models.Model):
	team = models.ForeignKey(Team)
	company = models.ForeignKey(Company)
	captain = models.CharField(max_length=100)
	captain_email = models.CharField(max_length=100)
	olympics = models.BooleanField(default=False)
	counter = models.BooleanField(default=False)
	tier = models.CharField(max_length=100, default=None, blank=True, null=True)
	datetime = models.DateTimeField(default=None, blank=True, null=True)

class Pledge(models.Model):
	sponsor = models.CharField(max_length=100, default='none', blank=True, null=True)
	participant = models.ForeignKey('Participant', default=None, blank=True, null=True)
	pledge_amount = models.DecimalField(default=Decimal('0.00'), max_digits=10, decimal_places=2, blank=True)
	max_pledge_amount = models.DecimalField(default=Decimal('0.00'), max_digits=10, decimal_places=2, blank=True)
	datetime = models.DateTimeField(default=None, blank=True, null=True)

class Counter(models.Model):

	WALK = 'WALK'
	RUN = 'RUN'

	TIER_TYPES = ((WALK, 'WALK'),(RUN, 'RUN'),)

	team = models.ForeignKey(Team)
	strip_id = models.PositiveIntegerField(default=0, blank=True, null=True)
	tier = models.CharField(max_length=100, choices=TIER_TYPES, default=WALK, blank=True, null=True)
	pledge_amount = models.DecimalField(default=Decimal('0.00'), max_digits=10, decimal_places=2, blank=True)
	max_pledge_amount = models.DecimalField(default=Decimal('0.00'), max_digits=10, decimal_places=2, blank=True)
	laps_completed = models.PositiveIntegerField(default=0, blank=True)
	total = models.DecimalField(default=Decimal('0.00'), max_digits=10, decimal_places=2, blank=True)
