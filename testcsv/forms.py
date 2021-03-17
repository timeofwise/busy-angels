from django import forms
from rich.models import Asset

class EventsForm(forms.ModelForm):

    class Meta:
        model = Asset
        fields = [
        ]