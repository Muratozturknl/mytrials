from django import forms
from .models import Zak
class ZakForm(forms.ModelForm):
    class Meta:
        model = Zak
        fields = ["task","amount"]

class PayForm(forms.ModelForm):
    class Meta:
        model = Zak
        fields = ["amount"]