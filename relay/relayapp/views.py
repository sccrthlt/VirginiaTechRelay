#vtrelay/relayapp
#TODO: add call for core/teams/greek
#TODO: aggregate the count of members for each team when passing object
import json

from django.db.models import Sum
from django.forms.models import model_to_dict

from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.template import RequestContext
from relayapp.models import *
from relayapp.RelayFunctions import *
from operator import itemgetter
from datetime import datetime
# from django.views.decorators.cache import cache_page

# @cache_page(60 * 60) # cache for 60 minutes
def participant_info(request):
	if request.method == 'GET':
		if 'email' in request.GET:
			participant_email = request.GET.get('email')
			participant = Participant.objects.get(email = participant_email)

			"""
			json_serializer = serializers.get_serializer("json")()
			response = json_serializer.serialize(participant, ensure_ascii=False)
			return HttpResponse(response, mimetype="application/json")
			"""

			response = HttpResponse()
			response.content = serialized_obj = serializers.serialize('json', [ participant, ])
			response['Content-Type'] = 'application/json'
			return response

##  if request.method == 'POST':
##      participant_email = request.POST.get('email', '')
##      numguests = request.POST.get('guests', '')
##      eventid = request.POST.get('event', '')
##
##      participantkey = Participant.objects.get(email = participant_email)
##      eventkey = Event.objects.get(id=eventid)
##      per = Participant_Event_Record(guests = numguests, event = eventkey, participant = participantkey)
##      per.save()
##
##      response = HttpResponse()
##      response.content = serialized_obj = serializers.serialize('json', [ per, ])
##      response['Content-Type'] = 'application/json'
##      return response

# @cache_page(60 * 60) # cache for 60 minutes
def all_participants_info(request):
	participants = Participant.objects.all()
	json_serializer = serializers.get_serializer("json")()
	response = json_serializer.serialize(participants, ensure_ascii=False)
	return HttpResponse(response, mimetype="application/json")

# @cache_page(60 * 60) # cache for 60 minutes
def all_teams_info(request):
	teams = Team.objects.all()
	json_serializer = serializers.get_serializer("json")()
	response = json_serializer.serialize(teams, ensure_ascii=False)
	return HttpResponse(response, mimetype="application/json")

# @cache_page(60 * 60) # cache for 60 minutes
def homepage_events(request):
	hpage_count = Event.objects.filter(homepage=True).count()
	if hpage_count >= 4:
		events = Event.objects.filter(homepage=True)[:4]
	else:
		events = Event.objects.filter(homepage=True)

	if hpage_count == 1:
		response = HttpResponse()
		response.content = serialized_obj = serializers.serialize('json', [ events, ])
		response['Content-Type'] = 'application/json'
		return response
	else:
		json_serializer = serializers.get_serializer("json")()
		response = json_serializer.serialize(events, ensure_ascii=False)
		return HttpResponse(response, mimetype="application/json")


# @cache_page(60 * 60) # cache for 60 minutes
def all_team_candles_general(request):
	helper = RelayFunctions()

	all_team_candles = []

	for company in Company.objects.filter(company_type = 'RT'):
		for team in Team.objects.filter(company = company):
			if team.signup == True:
				all_team_candles.append(helper.team_candles(model_to_dict(team)['id']))

	newlist = sorted(all_team_candles, key=itemgetter('team_candles_total'), reverse = True)

	currPos = 1
	for item in newlist:
		item['pos'] = currPos
		currPos = currPos + 1

	response = json.dumps(newlist)
	return HttpResponse(response, mimetype="application/json")

# @cache_page(60 * 60) # cache for 60 minutes
def team_singular_general(request, team):
	helper = RelayFunctions()

	cool = helper.team_candles(team)

	response = json.dumps(cool)
	return HttpResponse(response, mimetype="application/json")

# @cache_page(60 * 60) # cache for 60 minutes
def team_singular_greek(request, team):
	helper = RelayFunctions()

	cool = helper.company_specific_greek_candles(team)

	response = json.dumps(cool)
	return HttpResponse(response, mimetype="application/json")

# @cache_page(60 * 60) # cache for 60 minutes
def team_specific_general_candles(request, team):
	helper = RelayFunctions()

	all_team_specific_general_candles = []

	for participant in Participant.objects.filter(team = team):
			all_team_specific_general_candles.append(helper.team_specific_general_candles(model_to_dict(participant)['id']))
			cool = helper.team_specific_general_candles(model_to_dict(participant)['id'])

	newlist = sorted(all_team_specific_general_candles, key=itemgetter('participant_candles_total'), reverse = True)

	response = json.dumps(newlist)
	return HttpResponse(response, mimetype="application/json")

def team_specific_general_participants(request, team):
	helper = RelayFunctions()

	all_team_specific_general_participants = []

	for participant in Participant.objects.filter(team = team):
			all_team_specific_general_participants.append(helper.team_specific_general_participants(model_to_dict(participant)['id']))
			cool = helper.team_specific_general_participants(model_to_dict(participant)['id'])
			currTotal = cool.participant_candles_total

	##newlist = sorted(all_team_specific_general_participants, key=itemgetter('participant_candles_total'), reverse = True)

	response = json.dumps(all_team_specific_general_participants)
	return HttpResponse(response, mimetype="application/json")

def team_specific_greek_candles(request, team):
	helper = RelayFunctions()

	all_team_specific_greek_candles = []

	teamObject = Team.objects.get(pk = team)
	companyObject = Company.objects.get(pk = teamObject.company.id)
	for participant in Participant.objects.filter(team = team):
			all_team_specific_greek_candles.append(helper.team_specific_greek_candles(model_to_dict(participant)['id']))

	newlist = sorted(all_team_specific_greek_candles, key=itemgetter('participant_candles_total'), reverse = True)

	response = json.dumps(newlist)
	return HttpResponse(response, mimetype="application/json")

def company_specific_greek_candles(request, company):
	helper = RelayFunctions()

	all_company_specific_greek_candles = []

	for team in Team.objects.filter(company = company):
			all_company_specific_greek_candles.append(helper.company_specific_greek_candles(model_to_dict(team)['id']))

	newlist = sorted(all_company_specific_greek_candles, key=itemgetter('team_event_milestone_candles'), reverse = True)

	response = json.dumps(newlist)
	return HttpResponse(response, mimetype="application/json")

# @cache_page(60 * 60) # cache for 60 minutes
def all_candles(request):
	helper = RelayFunctions()

	all_candles_total = []

	for team in Team.objects.all():
			all_candles_total.append(helper.candles_total(model_to_dict(team)['id']))

	response = json.dumps(all_candles_total)
	return HttpResponse(response, mimetype="application/json")


# @cache_page(60 * 60) # cache for 60 minutes
def all_company_greek_candles(request):
	helper = RelayFunctions()

	all_company_greek_candles = []

	for company in Company.objects.filter(company_type = 'GT'):
			all_company_greek_candles.append(helper.company_greek_candles(model_to_dict(company)['id']))

	newlist = sorted(all_company_greek_candles, key=itemgetter('company_candles_total'), reverse = True)

	response = json.dumps(newlist)
	return HttpResponse(response, mimetype="application/json")


# @cache_page(60 * 60) # cache for 60 minutes
def company_singular_greek(request, company):
	helper = RelayFunctions()

	cool = helper.company_greek_candles(company)

	response = json.dumps(cool)
	return HttpResponse(response, mimetype="application/json")


# @cache_page(60 * 60) # cache for 60 minutes
def all_company_corps_candles(request):
	helper = RelayFunctions()

	all_company_corps_candles = []

	for company in Company.objects.filter(company_type = 'CT'):
			all_company_corps_candles.append(helper.company_corps_candles(model_to_dict(company)['id']))

	response = json.dumps(all_company_corps_candles)
	return HttpResponse(response, mimetype="application/json")

# @cache_page(60 * 60) # cache for 60 minutes
def teams_all(request):
	helper = RelayFunctions()
	
	teams = []
	for team in Team.objects.all():
		teams.append(helper.teams_all(model_to_dict(team)['id']))
		
	response = json.dumps(teams)
	return HttpResponse(response, mimetype="application/json")

# @cache_page(60 * 60) # cache for 60 minutes
def participant_specific(request, participant):
	helper = RelayFunctions()

	info = helper.participant_specific_info(participant)
	totals = helper.participant_specific_totals(participant)
	donations = helper.participant_specific_donations(participant)
	milestones = helper.participant_specific_milestones(participant)
	events = helper.participant_specific_events(participant)
	emails = helper.participant_specific_emails(participant)


	data = { 'info' : info , 'totals' : totals , 'donations' : donations , 'milestones' : milestones, 'events':events, 'emails':emails }

	response = json.dumps(data)
	return HttpResponse(response, mimetype="application/json")

# @cache_page(60 * 60) # cache for 60 minutes
def participant_specific_greek(request, participant):
	helper = RelayFunctions()

	info = helper.participant_specific_info_greek(participant)
	totals = helper.participant_specific_totals_greek(participant)
	donations = helper.participant_specific_donations_greek(participant)
	events = helper.participant_specific_events_greek(participant)
	tshirts = helper.participant_specific_tshirt_greek(participant)
	
	data = { 'info' : info , 'totals' : totals , 'donations' : donations , 'events' : events, 'tshirts' : tshirts }

	response = json.dumps(data)
	return HttpResponse(response, mimetype="application/json")

@csrf_exempt
def event_registration(request):
	participant_id = request.POST.get('id', '')
	numguests = request.POST.get('guests', '')
	eventid = request.POST.get('event', '')

	try:
		participantkey = Participant.objects.get(pk = participant_id)
	except Participant.DoesNotExist:
		return HttpResponse(status=400)

	eventkey = Event.objects.get(id=eventid)
	per = Participant_Event_Record(guests = numguests, event = eventkey, participant = participantkey)
	per.save()

	response = HttpResponse()
	response.content = serialized_obj = serializers.serialize('json', [ per, ])
	response['Content-Type'] = 'application/json'
	return response

@csrf_exempt
def team_registration(request):
	team_id = request.POST.get('team', '')
	signup = request.POST.get('signup', '')

	try:
		team = Team.objects.get(id = team_id)
		team.signup = signup.lower() in ("yes", "true", "t", "1")
		team.save()
	except Team.DoesNotExist:
		return HttpResponse(status=400)

	response = HttpResponse()
	response.content = serialized_obj = serializers.serialize('json', [ team, ])
	response['Content-Type'] = 'application/json'
	return response
	
def participant_unsigned(request):
	helper = RelayFunctions()
	
	participants = []
	for participant in Participant.objects.all():
		participants.append(helper.participants_unsigned(model_to_dict(participant)['id']))
		
	response = json.dumps(participants)
	return HttpResponse(response, mimetype="application/json")

@csrf_exempt
def myCandles_reg(request):
	username = request.POST.get('username', '')
	participant_id = request.POST.get('id', '')
	
	try:
		participant = Participant.objects.get(id = participant_id)
		participant.facebook_username = username
		participant.save()
	except Participant.DoesNotExist:
		return HttpResponse(status=400)
	
	response = HttpResponse()
	response.content = serialized_obj = serializers.serialize('json', [ participant, ])
	response['Content-Type'] = 'application/json'
	return response

@csrf_exempt
def counter_olympics_reg(request):
	team_id = request.POST.get('id', '')
	Counter = request.POST.get('signupCounter', '')
	signupCounter = Counter.lower() in ("yes", "true", "t", "1")
	Olympics = request.POST.get('signupOlympics', '')
	signupOlympics = Olympics.lower() in ("yes", "true", "t", "1")
	tier = request.POST.get('tier', '')
	

	try:
		team_object = Team.objects.get(pk = team_id)
		company_object = Company.objects.get(team = team_object)
		captain_fname = model_to_dict(Team_Captain.objects.get(team = team_object))['fname']
		captain_lname = model_to_dict(Team_Captain.objects.get(team = team_object))['lname']
		captain_name = captain_fname + ' ' + captain_lname
		captain_email = model_to_dict(Team_Captain.objects.get(team = team_object))['email']
			
		new_Olympics_Lap_Counter_Signup = Olympics_Lap_Counter_Signup(team = team_object, company = company_object, captain = captain_name, captain_email = captain_email, counter = signupCounter, olympics = signupOlympics, tier = tier, datetime = datetime.now())
		new_Olympics_Lap_Counter_Signup.save()
	except Olympics_Lap_Counter_Signup.DoesNotExist:
		print('uh oh')
	
	response = HttpResponse()
	response.content = serialized_obj = serializers.serialize('json', [ new_Olympics_Lap_Counter_Signup, ])
	response['Content-Type'] = 'application/json'
	return response
	
@csrf_exempt
def checkBackend(request):
	username = request.POST.get('username', '')
	
	try:
		participant_object = Participant.objects.get(facebook_username = username)
	except Participant.DoesNotExist:
		return HttpResponse(status=400)

	response = HttpResponse()
	response.content = serialized_obj = serializers.serialize('json', [ participant_object, ])
	response['Content-Type'] = 'application/json'
	return response

@csrf_exempt
def hokie_passport_reg(request):
	participant_id = request.POST.get('participantId', '')
	hokie_id = request.POST.get('hokiePassportId', '')
	
	try:
		participant = Participant.objects.get(pk = participant_id)
		participant.hokie_passport_id = hokie_id
		participant.save()
	except Participant.DoesNotExist:
		return HttpResponse(status=400)
	
	response = HttpResponse()
	response.content = serialized_obj = serializers.serialize('json', [ participant, ])
	response['Content-Type'] = 'application/json'
	return response

@csrf_exempt
def setupUser(request):
	first_name = request.POST.get('first_name', '')
	last_name = request.POST.get('last_name', '')
	email = request.POST.get('email', '')
	password = request.POST.get('password', '')
	
	try:
		user = User.objects.get(first_name = first_name, last_name = last_name , email = email, password = password)
	except User.DoesNotExist:
		user = User.objects.create_user(first_name = first_name, last_name = last_name , email = email, password = password)
	
	response = HttpResponse()
	response.content = serialized_obj = serializers.serialize('json', [ participant, ])
	response['Content-Type'] = 'application/json'
	return response

@csrf_exempt
def userSignIn(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
			# Redirect to a success page.
		else:
			return user
	else:
		return HttpResponse(status=400)
		
	response = HttpResponse()
	response.content = serialized_obj = serializers.serialize('json', [ user, ])
	response['Content-Type'] = 'application/json'
	return response

@csrf_exempt
def userSignOut(request):
	logout(request)
	# Redirect to a success page.
	

#def handle(self, *args, **options):
#helper = counter()
	
#print "Starting Command.."
#csv_file_location = args[0]
# print sys.getdefaultencoding()
#counter.parseCSVCounter(csv_file_location)