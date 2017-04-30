from django.forms import ModelForm
from django import forms

        
class madlib2Form(forms.Form):
    var1 = forms.CharField(label='Animal', max_length=20, required=True)
    var2 = forms.CharField(label='Food', max_length=20, required=True)
    var3 = forms.CharField(label='Noun', max_length=20, required=True)
    var4 = forms.CharField(label='Verb', max_length=20, required=True)
    var5 = forms.CharField(label='Verb', max_length=20, required=True)
    var6 = forms.CharField(label='Verb', max_length=20, required=True)
    var7 = forms.CharField(label='Verb', max_length=20, required=True)
    var8 = forms.CharField(label='Noun', max_length=20, required=True)
    var9 = forms.CharField(label='Location', max_length=20, required=True)
    var10 = forms.CharField(label='Noun', max_length=20, required=True)
    var11 = forms.CharField(label='Noun', max_length=20, required=True)
    var12 = forms.CharField(label='Location', max_length=20, required=True)
    var13 = forms.CharField(label='Verb', max_length=20, required=True)
    var14 = forms.CharField(label='Food', max_length=20, required=True)
    var15 = forms.CharField(label='Game', max_length=20, required=True)
    var16 = forms.CharField(label='Verb', max_length=20, required=True)
    var17 = forms.CharField(label='Noun', max_length=20, required=True)
    var18 = forms.CharField(label='Noun', max_length=20, required=True)
    var19 = forms.CharField(label='Plural Noun', max_length=20, required=True)
    var20 = forms.CharField(label="Verb Ending In 'ing'", max_length=20, required=True)
    var21 = forms.CharField(label='Verb', max_length=20, required=True)
    var22 = forms.CharField(label='Plural Noun', max_length=20, required=True)
    var23 = forms.CharField(label='Verb', max_length=20, required=True)
    
    
    # madlib2_email = forms.EmailField(required=True)
    # content = forms.CharField(required=True, widget=forms.Textarea)
    