from .models import Team, Player
from django import forms

class TeamForm(forms.ModelForm):

    class Meta:
        model = Team
        fields = ('team_name', 'league_name', 'season', 'division')
        
class PlayerForm(forms.ModelForm):

    class Meta:
        model = Player
        fields = ('player_name', 'player_number', 'player_position', 'team_id', 'username')