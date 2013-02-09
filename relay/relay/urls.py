from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('relay',
    # Examples:
    # url(r'^$', 'relay.views.home', name='home'),
    # url(r'^relay/', include('relay.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('relayapp.views',
	url(r'^participants/all/$', 'all_participants_info'),
	url(r'^participants/$', 'participant_info'),
	url(r'^events/registration/$', 'event_registration'),
	url(r'^events/homepage_events/$', 'homepage_events'),
        url(r'^participants/(?P<participant>\d{1,4})/$', 'participant_specific_info'),
	url(r'^teams/all/$', 'all_teams_info'),
        url(r'^teams/participants/(?P<team>\d{1,4})/$', 'team_participants'),
	url(r'^teams/registration/$', 'team_registration'),
        url(r'^teams/unregistered/$', 'teams_unregistered'),
        url(r'^teams/candles/all/$', 'all_team_candles'),
        url(r'^teams/candles/(?P<team>\d{1,4})/$', 'team_candles'),
        url(r'^companies/candles/all/$', 'all_company_candles'),
        url(r'^companies/corps/candles/all/$', 'all_company_corps_candles'),
        url(r'^companies/candles/(?P<company>\d{1,4})/$', 'company_candles'),
        url(r'^team/specific/candles/(?P<team>\d{1,4})/$', 'team_specific_general_candles'),
        url(r'^companies/donations/all/$', 'all_company_donations'),
        url(r'^participants/specific/(?P<team>\d{1,4})/$', 'participant_specific'),
        url(r'^candles/all/$', 'all_candles'),
)
