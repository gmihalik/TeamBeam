from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<team_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<team_id>[0-9]+)/roster/$', views.roster, name='roster'),
    url(r'^(?P<team_id>[0-9]+)/roster/player/(?P<player_id>[0-9]+)/$', views.player, name='player'),
]