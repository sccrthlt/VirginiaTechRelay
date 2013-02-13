#vtrelay/relayapp
#TODO: add call for core/teams/greek
#TODO: aggregate the count of members for each team when passing object
import json

from django.db.models import Sum
from django.forms.models import model_to_dict

from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from django.template import RequestContext
from relayapp.models import *
from relayapp.RelayFunctions import *
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
def participant_specific_info(request, participant):

	helper = RelayFunctions()
	info = helper.participant_specific_general_candles(participant)

	response = json.dumps(info)
	return HttpResponse(response, mimetype="application/json")

# @cache_page(60 * 60) # cache for 60 minutes
def team_participants(request, team):
	team_participants = Participant.objects.filter(team = team)

	json_serializer = serializers.get_serializer("json")()
	response = json_serializer.serialize(team_participants, ensure_ascii=False)
	return HttpResponse(response, mimetype="application/json")

# @cache_page(60 * 60) # cache for 60 minutes
def team_candles(request, team):
	helper = RelayFunctions()
	response = json.dumps(helper.team_candles(team))
	return HttpResponse(response, mimetype="application/json")

# @cache_page(60 * 60) # cache for 60 minutes
def all_team_candles(request, team):
	helper = RelayFunctions()

	all_team_candles = []

	for team in Team.objects.filter(team = team, signup = True):
			all_team_candles.append(helper.team_candles(model_to_dict(team)['id']))

	response = json.dumps(all_team_candles)
	return HttpResponse(response, mimetype="application/json")

# @cache_page(60 * 60) # cache for 60 minutes
def company_candles(request, company):
	helper = RelayFunctions()
	response = json.dumps(helper.company_candles(company))
	return HttpResponse(response, mimetype="application/json")

# @cache_page(60 * 60) # cache for 60 minutes
def team_specific_general_candles(request, team):
	helper = RelayFunctions()

	all_participant_specific_general_candles = []

	for participant in Participant.objects.filter(team = team):
			all_participant_specific_general_candles.append(helper.participant_specific_general_candles(model_to_dict(participant)['id']))

	response = json.dumps(all_participant_specific_general_candles)
	return HttpResponse(response, mimetype="application/json")

# @cache_page(60 * 60) # cache for 60 minutes
def all_candles(request):
	helper = RelayFunctions()

	all_candles_total = []

	for team in Team.objects.filter(team = team, signup = True):
			all_candles_total.append(helper.candles_total(model_to_dict(team)['id']))

	response = json.dumps(all_candles_total)
	return HttpResponse(response, mimetype="application/json")

# @cache_page(60 * 60) # cache for 60 minutes
def all_company_candles(request):
	helper = RelayFunctions()

	all_company_candles = []

	for company in Company.objects.all():
			all_company_candles.append(helper.company_candles(model_to_dict(company)['id']))

	response = json.dumps(all_company_candles)
	return HttpResponse(response, mimetype="application/json")

# @cache_page(60 * 60) # cache for 60 minutes
def all_company_corps_candles(request):
	helper = RelayFunctions()

	all_company_corps_candles = []

	for company in Company.objects.all():
			all_company_corps_candles.append(helper.company_corps_candles(model_to_dict(company)['id']))

	response = json.dumps(all_company_corps_candles)
	return HttpResponse(response, mimetype="application/json")

# @cache_page(60 * 60) # cache for 60 minutes
def all_company_donations(request):
	helper = RelayFunctions()

	all_company_donations = []

	for company in Company.objects.all():
			all_company_donations.append(helper.company_donations(model_to_dict(company)['id']))

	response = json.dumps(all_company_donations)
	return HttpResponse(response, mimetype="application/json")

def teams_unregistered(request):
	unregistered = Team.objects.filter(signup = False)

	teams = []
	for team in unregistered:
		team = model_to_dict(team)
		team['team_type'] = model_to_dict(Company.objects.get(team__pk = team['id']))['company_type']
		teams.append(team)

	#json_serializer = serializers.get_serializer("json")()
	#response = json_serializer.serialize(unregistered, ensure_ascii=False)
	response = json.dumps(teams)
	return HttpResponse(response, mimetype="application/json")

# @cache_page(60 * 60) # cache for 60 minutes
def participant_specific(request, participant):
	helper = RelayFunctions()

	donations = helper.participant_specific_donations(participant)
	milestones = helper.participant_specific_milestones(participant)
	events = helper.participant_specific_events(participant)
	emails = helper.participant_specific_emails(participant)


	data = { 'donations' : donations , 'milestones' : milestones, 'events':events, 'emails':emails }

	response = json.dumps(data)
	return HttpResponse(response, mimetype="application/json")

@csrf_exempt
def event_registration(request):
	participant_email = request.POST.get('email', '')
	numguests = request.POST.get('guests', '')
	eventid = request.POST.get('event', '')

	try:
		participantkey = Participant.objects.get(email = participant_email)
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
