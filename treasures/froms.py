from django import forms
from .models import treasureGram

class treasureForm(forms.ModelForm):
    class Meta:
        model = treasureGram
        fields = ['name', 'value', 'location', 'material', 'image_url']