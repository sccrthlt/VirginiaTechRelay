from django.core.mail import send_mail
from django.core.management.base import BaseCommand, CommandError
from relayapp.models import *
from django.db.models import Sum
from django.db.models import Count
from django.forms.models import model_to_dict
from django.contrib.auth.models import User




class Command(BaseCommand):
    args = 'CSV file with <Donation> detail data'
    help = 'Parses CSV files related to donation details'

    def handle(self, *args, **options):
        print "Starting Command.."
        sendemail()

def sendemail():
	user = User.objects.create_user('scott2@vt.edu', 'scott2@vt.edu', 'scottrules')
	user_email = user.email
	send_mail('Subject here', 'Here is the message.', 'vtrelay.productions@gmail.com',[user_email], fail_silently=False)