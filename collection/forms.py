from django.forms import ModelForm
from django import forms

from collection.models import Thing

class ThingForm(ModelForm):
    class Meta:
        model = Thing
        fields = ('name', 'description',)
        
class ContactForm(forms.Form):
    var1 = forms.CharField(label='Animal', required=True)
    var2 = forms.CharField(label='Food', required=True)
    var3 = forms.CharField(label='Noun', required=True)
    var4 = forms.CharField(label='Verb', required=True)
    var5 = forms.CharField(label='Verb', required=True)
    var6 = forms.CharField(label='Verb', required=True)
    var7 = forms.CharField(label='Verb', required=True)
    # contact_email = forms.EmailField(required=True)
    # content = forms.CharField(required=True, widget=forms.Textarea)
    