from django.template.loader import get_template
from django import template
from django.http import HttpResponse

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

def renderParticipant(request):
	t = get_template('base_participant.html')
	context = {'pagesButtonGeneral': 'generalUp', 
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
		'onLoad': 'cool()',
		'scrollbarID': ''
		}
	c = template.Context(context)
	r = t.render(c)
	return HttpResponse(r)