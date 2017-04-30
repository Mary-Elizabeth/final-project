from django.forms import ModelForm
from django import forms

from collection.models import Thing

class ThingForm(ModelForm):
    class Meta:
        model = Thing
        fields = ('name', 'description',)
        
class ContactForm(forms.Form):
    contact_name = forms.CharField(label='Your name', required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )
    