from django.contrib import admin

from .models import Team

# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    list_display = ['team_name','team_id','timestamp','updated']
    class Meta:
        model = Team

admin.site.register(Team, TeamAdmin)