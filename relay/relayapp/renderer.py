from django.template.loader import get_template
from django import template
from django.http import HttpResponse

def renderHome(request):
	#return render_template('teamList.html')
	t = get_template('base_home.html')
	c = template.Context({'name': 'Adrian'})
	r = t.render(c)
	return HttpResponse(r)

def renderTeamList(request):
	#return render_template('teamList.html')
	t = get_template('base_teamList.html')
	c = template.Context({'name': 'Adrian'})
	r = t.render(c)
	return HttpResponse(r)