from django.contrib import admin

from .models import Team
from .models import Player

# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    list_display = ['team_name','team_id','timestamp','updated']
    class Meta:
        model = Team

class PlayerAdmin(admin.ModelAdmin):
    list_display = ['player_name','player_number','player_position','email','team_id','timestamp','updated']
    class Meta:
        model = Player
        
admin.site.register(Team, TeamAdmin)
admin.site.register(Player, PlayerAdmin)