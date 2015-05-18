from django.db import models
from teams.models import Team
from django.contrib.auth.models import User

class League(models.Model):
    league_name = models.CharField(max_length=200)
    team_id = models.ForeignKey(Team)
    season = models.CharField(max_length=200,default='None')
    division = models.CharField(max_length=200,default='None')
    current = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
    updated = models.DateTimeField(auto_now_add = False, auto_now = True)
    
    def __unicode__(self):
        return self.league_name

class Event(models.Model):
    event_name= models.CharField(max_length=200)
    event_date = models.DateTimeField(auto_now_add = False, auto_now = True)
    event_location = models.CharField(max_length=200)
    event_time = models.DateTimeField(auto_now_add = False, auto_now = True)
    event_is_game= models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
    updated = models.DateTimeField(auto_now_add = False, auto_now = True)
    
    def __unicode__(self):
        return self.event_name