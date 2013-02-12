#relay/relayapp
from django.db import models
from decimal import Decimal

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

class Participant(models.Model):
    fname = models.CharField(verbose_name='First Name', max_length=100)
    lname = models.CharField(verbose_name='Last Name', max_length=100)
    email = models.EmailField(blank=False)
    #milestone can be figured from data
    emails_sent = models.PositiveIntegerField(default=0, blank=True)
    team = models.ForeignKey(Team)
    reg_date = models.DateField()
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
    candles_rewarded = models.IntegerField()
    description = models.TextField(blank=True)
    image = models.URLField(blank = True)
    homepage = models.BooleanField()

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['date']

#change to partipant record for donations
#pull from CSV
class TShirt(models.Model):
    name = models.CharField(max_length=200)

class Donation(models.Model):
    participant = models.ForeignKey(Participant)
    amount = models.DecimalField(default=Decimal('0.00'), max_digits=10, decimal_places=2, blank=True)
    date = models.DateField()

class Company_TShirt_Milestone(models.Model):
    percentage_purchased = models.PositiveIntegerField(default=0, blank=True)
    candles_rewarded = models.PositiveIntegerField()

class Donation_Milestone(models.Model):
    donation_amount = models.DecimalField(default=Decimal('0.00'), max_digits=10, decimal_places=2, blank=True)
    candles_rewarded = models.PositiveIntegerField()

    def __unicode__(self):
        return 'Milestone: ' + str(self.donation_amount) + ' Candles: ' + str(self.candles_rewarded)

    class Meta:
        ordering = ['candles_rewarded']

class Company_Registration_Rule(models.Model):
    percent_registered = models.PositiveIntegerField(default=0, blank=True)
    candles_rewarded = models.PositiveIntegerField()
    date_cutoff = models.DateField()

class Email_Rule(models.Model):
    candles_rewarded = models.PositiveIntegerField()
    emails = models.PositiveIntegerField()

    def __unicode__(self):
        return 'Emails: ' + str(self.emails) + ' Candles: ' + str(self.candles_rewarded)

class Participant_Email_Record(models.Model):
    participant = models.ForeignKey(Participant)
    email_milestone = models.ForeignKey(Email_Rule)
    date = models.DateField()

class Participant_Event_Record(models.Model):
    guests = models.PositiveIntegerField(default=0, blank=True)
    event = models.ForeignKey(Event)
    participant = models.ForeignKey(Participant)

class Company_TShirt_Milestone_Record(models.Model):
    company = models.ForeignKey(Company)
    tshirt_milestone = models.ForeignKey(Company_TShirt_Milestone)
    date = models.DateField()

class Team_Event_Record(models.Model):
    event = models.ForeignKey(Event)
    team = models.ForeignKey(Team)

class Participant_Milestone_Record(models.Model):
    participant = models.ForeignKey(Participant)
    donation_milestone = models.ForeignKey(Donation_Milestone)
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

#add tshirt milestone record for copmanies

#participant percentage registration milestone company
