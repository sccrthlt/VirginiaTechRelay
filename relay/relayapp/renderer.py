from django.template.loader import get_template
from django import template
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.shortcuts import render
from relayapp.models import *
from relayapp.RelayFunctions import *
from django.db.models import Sum
from django.db.models import Count
from django.forms.models import model_to_dict
import urllib

def renderRedirectHome(request):
	t = get_template('base_redirect.html')
	context = {'pagesButtonGeneral': 'generalDown', 
		'pagesButtonGreek': 'greeksDown', 
		'pagesButtonCorps': 'corpsDown', 
		'onLoad': 'cool()',
		'scrollbarID': '#forScroll',
		'redirectUrl': 'http://vtrelaycandles.org/home',
		}
	c = template.Context(context)
	r = t.render(c)
	return HttpResponse(r)

def renderRedirectSignup(request):
	t = get_template('base_redirect.html')
	context = {'pagesButtonGeneral': 'generalDown', 
		'pagesButtonGreek': 'greeksDown', 
		'pagesButtonCorps': 'corpsDown', 
		'onLoad': 'cool()',
		'scrollbarID': '#forScroll',
		'redirectUrl': 'http://vtrelaycandles.org/signup',
		}
	c = template.Context(context)
	r = t.render(c)
	return HttpResponse(r)
	
def renderRedirectTeamList(request):
	t = get_template('base_redirect.html')
	context = {'pagesButtonGeneral': 'generalDown', 
		'pagesButtonGreek': 'greeksDown', 
		'pagesButtonCorps': 'corpsDown', 
		'onLoad': 'cool()',
		'scrollbarID': '#forScroll',
		'redirectUrl': 'http://vtrelaycandles.org/teamList',
		}
	c = template.Context(context)
	r = t.render(c)
	return HttpResponse(r)

def renderRedirectGreekList(request):
	t = get_template('base_redirect.html')
	context = {'pagesButtonGeneral': 'generalDown', 
		'pagesButtonGreek': 'greeksDown', 
		'pagesButtonCorps': 'corpsDown', 
		'onLoad': 'cool()',
		'scrollbarID': '#forScroll',
		'redirectUrl': 'http://vtrelaycandles.org/greekList',
		}
	c = template.Context(context)
	r = t.render(c)
	return HttpResponse(r)

def renderHome(request):
	t = get_template('base_home.html')
	context = {'pagesButtonGeneral': 'generalDown', 
		'pagesButtonGreek': 'greeksDown', 
		'pagesButtonCorps': 'corpsDown', 
		'onLoad': 'setupPage()',
		'scrollbarID': '#forScroll'
		}
	c = template.Context(context)
	r = t.render(c)
	return HttpResponse(r)

def renderHomeNew(request):
	events = Event.objects.all()
	t = get_template('base_home_new.html')
	context = {'pagesButtonGeneral': 'generalDown', 
		'pagesButtonGreek': 'greeksDown', 
		'pagesButtonCorps': 'corpsDown', 
		'onLoad': 'setupPage()',
		'scrollbarID': '#forScroll',
		'events': events
		}
	c = template.Context(context)
	r = t.render(c)
	return HttpResponse(r)

def renderTeamList(request):
	t = get_template('base_teamList.html')
	context = {'pagesButtonGeneral': 'generalUp', 
		'pagesButtonGreek': 'greeksDown', 
		'pagesButtonCorps': 'corpsDown', 
		'onLoad': 'setupPage()',
		'scrollbarID': '#forScroll'
		}
	c = template.Context(context)
	r = t.render(c)
	return HttpResponse(r)
	
def renderGreekList(request):
	t = get_template('base_greekList.html')
	context = {'pagesButtonGeneral': 'generalDown', 
		'pagesButtonGreek': 'greeksUp', 
		'pagesButtonCorps': 'corpsDown', 
		'onLoad': 'setupPage()',
		'scrollbarID': '#forScroll'
		}
	c = template.Context(context)
	r = t.render(c)
	return HttpResponse(r)

def renderHowItWorks(request):
	t = get_template('base_howitworks.html')
	context = {'pagesButtonGeneral': 'generalDown', 
		'pagesButtonGreek': 'greeksDown', 
		'pagesButtonCorps': 'corpsDown', 
		'onLoad': 'cool()',
		'scrollbarID': '#forScroll'
		}
	c = template.Context(context)
	r = t.render(c)
	return HttpResponse(r)

def renderHowItWorksGeneral(request):
	t = get_template('base_howitworksGeneral.html')
	context = {'pagesButtonGeneral': 'generalDown', 
		'pagesButtonGreek': 'greeksDown', 
		'pagesButtonCorps': 'corpsDown'
		}
	c = template.Context(context)
	r = t.render(c)
	return HttpResponse(r)

def renderHowItWorksGreek(request):
	t = get_template('base_howitworksGreek.html')
	context = {'pagesButtonGeneral': 'generalDown', 
		'pagesButtonGreek': 'greeksDown', 
		'pagesButtonCorps': 'corpsDown'
		}
	c = template.Context(context)
	r = t.render(c)
	return HttpResponse(r)

def renderHowItWorksCorps(request):
	t = get_template('base_howitworksCorps.html')
	context = {'pagesButtonGeneral': 'generalDown', 
		'pagesButtonGreek': 'greeksDown', 
		'pagesButtonCorps': 'corpsDown'
		}
	c = template.Context(context)
	r = t.render(c)
	return HttpResponse(r)

def renderSignup(request):
	t = get_template('base_signup.html')
	context = {'pagesButtonGeneral': 'generalDown', 
		'pagesButtonGreek': 'greeksDown', 
		'pagesButtonCorps': 'corpsDown', 
		'onLoad': 'setupSignUpPage()',
		'scrollbarID': '#forScroll'
		}
	c = template.Context(context)
	r = t.render(c)
	return HttpResponse(r)

def renderSignupCounterReg(request):
	t = get_template('base_counterReg.html')
	context = {'pagesButtonGeneral': 'generalDown', 
		'pagesButtonGreek': 'greeksDown', 
		'pagesButtonCorps': 'corpsDown', 
		'onLoad': 'setupCounterRegPage()'
		}
	c = template.Context(context)
	r = t.render(c)
	return HttpResponse(r)
	
def renderSignIn(request):
	t = get_template('base_signin.html')
	context = {'pagesButtonGeneral': 'generalDown', 
		'pagesButtonGreek': 'greeksDown', 
		'pagesButtonCorps': 'corpsDown', 
		'onLoad': 'setupCounterRegPage()'
		}
	c = template.Context(context)
	r = t.render(c)
	return HttpResponse(r)

def renderMyCandlesPage(request, User):
	participant = Participant.objects.get(pk = User)
	pledges = Pledge.objects.filter(participant = participant)
	
	if request.user.is_authenticated():
		if request.user.username == User:
			# Do something for authenticated users.
			t = get_template('base_myCandles.html')
			context = {'pagesButtonGeneral': 'generalDown', 
				'pagesButtonGreek': 'greeksDown', 
				'pagesButtonCorps': 'corpsDown', 
				'onLoad': 'cool()',
				'pledges': pledges,
				'participant': participant
				}
			c = template.Context(context)
			r = t.render(c)
			return HttpResponse(r)
		else:
			print('user is authenticated but not under this username')
			return render(request, 'base_login.html')
	else:
		print('user is not authenticated')
		return render(request, 'base_login.html')
		
def renderLogin(request):
	t = get_template('base_login.html')
	context = {'pagesButtonGeneral': 'generalDown', 
		'pagesButtonGreek': 'greeksDown', 
		'pagesButtonCorps': 'corpsDown', 
		'onLoad': 'setupCounterRegPage()'
		}
	c = template.Context(context)
	r = t.render(c)
	return HttpResponse(r)

def renderPledge(request):
	t = get_template('base_pledge.html')
	context = {'pagesButtonGeneral': 'generalDown', 
		'pagesButtonGreek': 'greeksDown', 
		'pagesButtonCorps': 'corpsDown', 
		'onLoad': 'setupMyCandlesRegPage()'
		}
	c = template.Context(context)
	r = t.render(c)
	return HttpResponse(r)
	
def renderCounter(request):
	walkers = Counter.objects.all(tier = 'walk')
	runners = Counter.objects.all(tier = 'run')
	
	t = get_template('base_counter.html')
	context = {'pagesButtonGeneral': 'generalDown', 
		'pagesButtonGreek': 'greeksDown', 
		'pagesButtonCorps': 'corpsDown', 
		'onLoad': 'setupCounterRegPage()',
		'teams': teams
		}
	c = template.Context(context)
	r = t.render(c)
	return HttpResponse(r)

def renderPassChange(request, User):
	participant = Participant.objects.get(pk = User)
	
	t = get_template('base_passchange.html')
	context = {'pagesButtonGeneral': 'generalDown', 
		'pagesButtonGreek': 'greeksDown', 
		'pagesButtonCorps': 'corpsDown', 
		'onLoad': 'cool()',
		'participant': participant
		}
	c = template.Context(context)
	r = t.render(c)
	return HttpResponse(r)
	
def renderSendEmail(request):
	
	t = get_template('base_sendemail.html')
	context = {'pagesButtonGeneral': 'generalDown', 
		'pagesButtonGreek': 'greeksDown', 
		'pagesButtonCorps': 'corpsDown', 
		'onLoad': 'cool()'
		}
	c = template.Context(context)
	r = t.render(c)
	return HttpResponse(r)