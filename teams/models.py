from django.db import models

# Create your models here.
class Team(models.Model):
    team_name = models.CharField(max_length=200)
    team_id = models.CharField(max_length=120,default='ABC')
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
    updated = models.DateTimeField(auto_now_add = False, auto_now = True)
    
    def __unicode__(self):
        return self.team_id
        
    class Meta:
        unique_together = ("team_name", "team_id")

class Player(models.Model):
    player_name = models.CharField(max_length=200)
    player_number = models.IntegerField(default=0)
    player_position = models.CharField(max_length=1)
    email = models.EmailField(unique=True)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
    updated = models.DateTimeField(auto_now_add = False, auto_now = True)
    team_id = models.ForeignKey(Team)
    
    def __str__(self):
        return self.player_name
    
class Event(models.Model):
    event_name = models.CharField(max_length=200)
    date = models.DateTimeField()
    location = models.CharField(max_length=250)
    
    def __str__(self):
        return self.event_name