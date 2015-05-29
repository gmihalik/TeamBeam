from .forms import TeamForm, PlayerForm
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from .models import Player, Team
from leagues.models import Event, League
from django.contrib.auth.models import User
import uuid
from django.db.models import F, Q
import datetime

def index(request):
    if request.user.is_authenticated():
        #Use the username to select all teams the user is on
        #use the team ids to make a list of all teams for the user
        player_username = User.objects.get(username=request.user.username)
        team_list = Team.objects.all().filter(player__username=player_username)
        context = {'team_list': team_list}
        template = "teams/dashboard.html"
        return render(request, template, context)
    else:
        return HttpResponseRedirect('/login')

def detail(request, team_id):
    if request.user.is_authenticated():
        if access_allowed(request, team_id):
            active = {'overview':'active'}
            team = Team.objects.get(team_id=team_id)
            print team_id
            today = datetime.datetime.today()
            event_list = Event.objects.all().order_by('event_date').filter(team_id=team).filter(Q(event_date__gte=today))
            #return HttpResponse("youre looking at team %s" % team.team_name)
            #template = loader.get_template('teams/team_home.html')
            context = {'team':team, 'team_id': team_id, 'active':active, 'event_list':event_list}
            template = "teams/team_home.html"
            return render(request, template, context)
        else:
            return HttpResponseRedirect('/teams')    
    else:
        return HttpResponseRedirect('/login')
        
def roster(request, team_id):
    '''
    output = ', '.join([p.player_name for p in team_list])
    team = Team.objects.get(id=team_id_id)
    output += '%s' % team.team_name'''
    '''
    team_list = Player.objects.all().filter(team_id=team_id)
    output = team_list
    return HttpResponse(output)
    '''
    if request.user.is_authenticated():
        if access_allowed(request, team_id):
            active = {'roster':'active'}
            player_team = Team.objects.get(team_id=team_id)
            #team_list = Player.objects.all().filter(team_id=player_team)
            #email_list = Player.objects.filter(team_id=player_team, username__username='').select_related()
            #email_list = User.objects.all().filter(player__team_id=player_team).select_related()
            #team_list = Player.objects.filter(team_id=player_team)
            #email_list = Player.objects.filter(team_id=player_team)
            #email_list = User.objects.select_related('username')
            #Entry.objects.filter(authors__name=F('blog__name'))
            #Entry.objects.filter(authors__name=F('player__username'))
            #email_list = User.objects.filter(player__username__in=team_list)
            team = Team.objects.get(team_id=team_id)
            players = set()
            
            for e in Player.objects.filter(team_id=player_team).all().select_related():
            # Without select_related(), this would make a database query for each
            # loop iteration in order to fetch the related blog for each entry.
                players.add(e)
            
            context = {'team_list': players, 'team_id': team_id, 'team': team, 'active':active}
            template = "teams/roster.html"
            return render(request, template, context)
        else:
            return HttpResponseRedirect('/teams')    
    else:
        return HttpResponseRedirect('/login')
def player(request, team_id, player_id):
    active = {'roster':'active'}
    if request.user.is_authenticated():
        team = Team.objects.get(team_id=team_id)
        player = Player.objects.get(id=player_id)
        template = loader.get_template('teams/players.html')
        context = RequestContext(request, {
            'player': player, 'team':team, 'team_id':team.team_id,'active':active
        })
        return HttpResponse(template.render(context))
    else:
        return HttpResponseRedirect('/login')
def create_team(request):
    if request.user.is_authenticated():
        context = RequestContext(request)
        team_created = False
        if request.method == 'POST':
            team_form = TeamForm(data=request.POST)
            if team_form.is_valid():
                team = team_form.save()
                team.team_id = get_team_id()
                team.save()
                team_created = True
                
                player_team = Team.objects.get(team_id=team.team_id)
                #player_username = str(request.user.username)
                player_username = User.objects.get(username=request.user.username)
                player_name = '%s %s' % (player_username.first_name, player_username.last_name)
                new_player = Player.objects.create(username= player_username, team_id_id = player_team.id, player_name=player_name)
                new_player.save()
                #add func for saving logged in user to player list
            else:
                print team_form.errors
                return render_to_response(
                'dashboard.html',
                {'team_form': team_form, 'team_created': team_created},
                context)
            return HttpResponseRedirect('/teams/')
        else:
         #   team_form = TeamForm()
            return HttpResponseRedirect('/teams/')
        #return render_to_response(
        #        'teams/create_team.html',
        #        {'team_form': team_form, 'team_created': team_created},
        #        context)
    else:
        return HttpResponseRedirect('/login')

def join_team(request):
    if request.user.is_authenticated():
        joined_team = False
        if request.method == 'POST':
            #add field validation and attemp to fix this to work with FORMS.py
            player_team = Team.objects.get(team_id=request.POST["team_id"])
            player_username = User.objects.get(username=request.POST["username"])
            new_player = Player(username=player_username, team_id=player_team, player_name = request.POST["player_name"], player_number=request.POST["player_number"], player_position=request.POST["player_position"])
            new_player.save()
            return HttpResponseRedirect('/teams/')
        else:
            return HttpResponseRedirect('/teams/')
    else:
        return HttpResponseRedirect('/login')

def events(request, team_id):
    active = {'schedule':'active'}
    team = Team.objects.get(team_id=team_id)
    today = datetime.datetime.today()
    event_list = Event.objects.all().order_by('event_date').filter(team_id=team).filter(Q(event_date__gte=today))
    
    #return HttpResponse("youre looking at team %s" % team.team_name)
    #template = loader.get_template('teams/team_home.html')
    context = {'team':team, 'team_id': team_id, 'active':active, 'event_list':event_list}
    template = "leagues/events.html"
    return render(request, template, context)

def create_event(request, team_id):
    if request.user.is_authenticated():
        context = RequestContext(request)
        new_event_created = False
        if request.method == 'POST':
            event_name = request.POST['event_name']
            event_date = request.POST['event_date']
            event_location = request.POST['event_location']
            event_time = request.POST['event_time']
            if request.POST.get('event_is_game'):
                event_is_game = True
            else:
                event_is_game = False
            #event_opponent = request.POST['event_opponent']
            team = Team.objects.get(team_id=team_id)
            team_id = team
            league = League.objects.all()#.filter(team_id=team).filter(current=True)
            print league[0]
            league_id = league[0]
            print event_date
            event_date = event_date + " " + event_time
            event_time = event_date
            print event_time
            new_event = Event.objects.create(event_name= event_name, event_date = event_date,  \
            event_location=event_location, event_time=event_time, event_is_game=event_is_game, \
            league_id=league_id, team_id=team_id)
            new_event.save()
            new_event_created = True
            return HttpResponseRedirect('/teams/%s/schedule'% team_id)
        else:
         #   team_form = TeamForm()
            return HttpResponseRedirect('/teams/%s/schedule'% team_id)

def get_team_id():
    team_id = str(uuid.uuid4())
    try:
        id_exists = Team.objects.get(team_id=team_id)
        get_team_id()
    except:
        return team_id
        
def access_allowed(request, team_id):
    player_username = User.objects.get(username=request.user.username)
    player_team = Team.objects.get(team_id=team_id)
    try:
        valid_player = Player.objects.get(username=player_username, team_id=player_team)
        return True
    except:
        return False
