from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Player, Team

def index(request):
    return HttpResponse("Hello world! teams index")
    

def detail(request, team_id):
    team = Team.objects.get(id=team_id)
    
    return HttpResponse("youre looking at team %s" % team.team_name)

def roster(request, team_id):

    '''team_list = Player.objects.all().filter(team_id_id=team_id_id)
    
    #output = team_list
    
    output = ', '.join([p.player_name for p in team_list])
    team = Team.objects.get(id=team_id_id)
    output += '%s' % team.team_name'''
    '''
    team_list = Player.objects.all().filter(team_id=team_id)
    output = team_list
    return HttpResponse(output)
    '''
    team_list = Player.objects.all().filter(team_id=team_id)
    template = loader.get_template('teams/roster.html')
    context = RequestContext(request, {
        'team_list': team_list,
    })
    return HttpResponse(template.render(context))
    
def player(request, team_id, player_id):
    team = Team.objects.get(id=team_id)
    player = Player.objects.get(id=player_id)
    template = loader.get_template('teams/players.html')
    context = RequestContext(request, {
        'player': player, 'team':team.team_name
    })
    return HttpResponse(template.render(context))
# Create your views here.
