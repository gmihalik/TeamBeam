from django.contrib import admin

from .models import League
from .models import Event
from .models import Availability
# Register your models here.
class LeagueAdmin(admin.ModelAdmin):
    #list_display = ['team_name','team_id','timestamp','updated']
    list_display = ['league_name','team_id','season','current','division','league_id','timestamp','updated']
    class Meta:
        model = League

class EventAdmin(admin.ModelAdmin):
    list_display = ['event_name','event_date','event_location','event_time','event_is_game','event_opponent','league_id','timestamp','updated']
    class Meta:
        model = Event

class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ['event_id','player_id','availability','timestamp','updated']
    class Meta:
        model = Event
        
admin.site.register(Availability, AvailabilityAdmin)
admin.site.register(League, LeagueAdmin)
admin.site.register(Event, EventAdmin)