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
    url(r'^candles/all/$', 'all_candles'),
    url(r'^participants/all/info/$', 'all_participants_info'),
    url(r'^participants/$', 'participant_info'),
    url(r'^teams/all/info/$', 'all_teams_info'),
    url(r'^events/registration/$', 'event_registration'),
    url(r'^events/homepage_events/$', 'homepage_events'),
    url(r'^teams/registration/$', 'team_registration'),
    url(r'^teams/unregistered/$', 'teams_unregistered'),
    url(r'^teams/candles/all/$', 'all_team_candles_general'),
    url(r'^teams/candles/all/corps/$', 'all_team_candles_corps'),
    url(r'^companies/greek/candles/all/$', 'all_company_greek_candles'),
    url(r'^companies/corps/candles/all/$', 'all_company_corps_candles'),
    url(r'^company/specific/greek/(?P<company>\d{1,4})/$', 'company_specific_greek_candles'),
    url(r'^team/specific/general/(?P<team>\d{1,4})/$', 'team_specific_general_candles'),
    url(r'^team/specific/general/participants/(?P<team>\d{1,4})/$', 'team_specific_general_participants'),
    url(r'^team/specific/greek/(?P<team>\d{1,4})/$', 'team_specific_greek_candles'),
    url(r'^participants/specific/(?P<participant>\d{1,4})/$', 'participant_specific'),
    url(r'^participants/specific/greek/(?P<participant>\d{1,4})/$', 'participant_specific_greek'),
    
)
