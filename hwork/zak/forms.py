from django import forms
from .models import Zak
class ZakForm(forms.ModelForm):
    class Meta:
        model = Zak
        fields = ["task","amount"]