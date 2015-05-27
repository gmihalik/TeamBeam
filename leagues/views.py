from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from .models import League, Event
from teams.models import Team, Player
from django.contrib.auth.models import User
import uuid
from django.db.models import F

def events(request, team_id):
    active = {'schedule':'active'}
    team = Team.objects.get(team_id=team_id)
    event_list = Event.objects.all().filter(team_id=team)
    #return HttpResponse("youre looking at team %s" % team.team_name)
    #template = loader.get_template('teams/team_home.html')
    context = {'team':team, 'team_id': team_id, 'active':active, 'event_list':event_list}
    template = "leagues/events.html"
    return render(request, template, context)