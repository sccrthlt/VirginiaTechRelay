from django.core.mail import send_mail
from django.core.management.base import BaseCommand, CommandError
from relayapp.models import *
from relayapp.RelayFunctions import *
from django.db.models import Sum
from django.db.models import Count
from django.forms.models import model_to_dict
from django.contrib.auth.models import User, Group




class Command(BaseCommand):
    args = 'CSV file with <Donation> detail data'
    help = 'Parses CSV files related to donation details'

    def handle(self, *args, **options):
        print "Starting Command.."
        #s = model_to_dict(Participant.objects.get(email = 'scott2@vt.edu'))['id']
        #setupUser()
        counter()

##def delete():
	##Pledge.objects.all().delete()

#def sendemail():
	#for team in Olympics_Lap_Counter_Signup.objects.all():
		#for participant in Participant.objects.filter(team = team):
			#x = participant.pk
			#user = User.objects.get(username = x)
			#username = str(user.username)
			#user_email = user.email
			#message = 'One of your VT Relay team members has signed your team up for the lap counter.  Did you know the lap counter is potentially a HUGE fundraiser for your team?  Laps = Money. Ask your friends and family to donate a small amount per lap (called a "Pledge"). Pledge here: http://vtrelaycandles.org/pledge/'
			#send_mail('Lap Counter Pledge', message, 'vtrelay.productions@gmail.com',[user_email], fail_silently=False, auth_user = 'no-reply@vtrelaycandles.org', auth_password = 'vtrelayexec')

def counter():
	helper = RelayFunctions()

	for o in Olympics_Lap_Counter_Signup.objects.all():
		team_id = o.team.pk
		team_object = Team.objects.get(pk = team_id)
		try:
			new_counter = Counter.objects.get(team = team_id)
		except Counter.DoesNotExist:
			print('Creating new')
			number = 0
			for counter in Counter.objects.all():
				number = number + 1
			number = number + 1
		
			counter_pledge_numbers = helper.counter(team_id)
			tier = o.tier
			pledge_amount = counter_pledge_numbers['pledge_amount']
			max_pledge_amount = counter_pledge_numbers['max_pledge_amount']
		
			new_counter = Counter(team = team_object, strip_id = number, tier = 'WALK', pledge_amount = pledge_amount, max_pledge_amount = max_pledge_amount, laps_completed = int(0))
			new_counter.save()
			
#def setupUser():
	#for participant in Participant.objects.all():
		#username = participant.pk
		#email = participant.email
		#groups = Group.objects.get(name = 'myCandles')

		#try:
			#user = User.objects.get(username = username)
		#except User.DoesNotExist:
			#new_user = User.objects.create_user(username = username, email = email, password = 'password')
			#new_user.group = groups
			#new_user.save()
			
