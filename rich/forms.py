from django import forms
from .models import Cashflow

class ExchangeForm(forms.ModelForm):


    class Meta:
        model = Cashflow
        fields = [
            'date',
            'io',
            'cash_krw',
            'cash_usd',
        ]
