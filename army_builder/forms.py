from django import forms
from .models import Roster, Ruleset, Army

class RosterForm(forms.ModelForm):
    class Meta:
        model = Roster
        fields = ["name", "ruleset", "army", "points_max"]
