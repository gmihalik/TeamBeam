from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^join/$', views.join_team, name='join_team'),
    url(r'^create/$', views.create_team, name='create_team'),
    url(r'^(?P<team_id>[a-zA-Z0-9-_]+)/$', views.detail, name='detail'),
    url(r'^(?P<team_id>[a-zA-Z0-9-_]+)/roster/$', views.roster, name='roster'),
    url(r'^(?P<team_id>[a-zA-Z0-9-_]+)/roster/player/(?P<player_id>[0-9]+)/$', views.player, name='player'),
    url(r'^(?P<team_id>[a-zA-Z0-9-_]+)/schedule/$', views.events, name='events'),
]