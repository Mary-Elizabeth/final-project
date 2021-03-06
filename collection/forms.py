from django.forms import ModelForm
from django import forms

class madlib1Form(forms.Form):
    ml1var1 = forms.CharField(label='Noun', max_length=20, required=True)
    ml1var2 = forms.CharField(label='Adjective', max_length=20, required=True)
    ml1var3 = forms.CharField(label='Verb', max_length=20, required=True)
    ml1var4 = forms.CharField(label='Adverb', max_length=20, required=True)
    ml1var5 = forms.CharField(label='Noun', max_length=20, required=True)
    ml1var6 = forms.CharField(label='Adjective', max_length=20, required=True)
    ml1var7 = forms.CharField(label='Plural Noun', max_length=20, required=True)
    ml1var8 = forms.CharField(label='Plural Noun', max_length=20, required=True)
    ml1var9 = forms.CharField(label='Plural Noun', max_length=20, required=True)
    ml1var10 = forms.CharField(label='Part of the Body', max_length=20, required=True)
    ml1var11 = forms.CharField(label='Noun', max_length=20, required=True)
    ml1var12 = forms.CharField(label='Noun', max_length=20, required=True)
    ml1var13 = forms.CharField(label='Noun', max_length=20, required=True)
    ml1var14 = forms.CharField(label='Noun', max_length=20, required=True)
    ml1var15 = forms.CharField(label='Part of the Body', max_length=20, required=True)
   
            
        
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
    var20 = forms.CharField(label="Verb Ending in 'ing'", max_length=20, required=True)
    var21 = forms.CharField(label='Verb', max_length=20, required=True)
    var22 = forms.CharField(label='Plural Noun', max_length=20, required=True)
    var23 = forms.CharField(label='Verb', max_length=20, required=True)
    
    
    
class madlib3Form(forms.Form):
    ml3var1 = forms.CharField(label='Adjective', max_length=20, required=True)
    ml3var2 = forms.CharField(label='Noun', max_length=20, required=True)
    ml3var3 = forms.CharField(label='Plural Noun', max_length=20, required=True)
    ml3var4 = forms.CharField(label='Adjective', max_length=20, required=True)
    ml3var5 = forms.CharField(label='Adjective', max_length=20, required=True)
    ml3var6 = forms.CharField(label="Verb Ending in 'ing'", max_length=20, required=True)
    ml3var7 = forms.CharField(label="Verb Ending in 'ing'", max_length=20, required=True)
    ml3var8 = forms.CharField(label='Adjective', max_length=20, required=True)
    ml3var9 = forms.CharField(label='Adjective', max_length=20, required=True)
    ml3var10 = forms.CharField(label='Noun', max_length=20, required=True)
    ml3var11 = forms.CharField(label='Food (Plural)', max_length=20, required=True)
    ml3var12 = forms.CharField(label='Part of the Body (Plural)', max_length=20, required=True)
    ml3var13 = forms.CharField(label='Adjective', max_length=20, required=True)
    ml3var14 = forms.CharField(label='Vehicle', max_length=20, required=True)
    ml3var15 = forms.CharField(label='Food (Plural)', max_length=20, required=True)
    ml3var16 = forms.CharField(label='Food (Plural)', max_length=20, required=True)
    ml3var17 = forms.CharField(label='Something Alive (Plural)', max_length=20, required=True)
    ml3var18 = forms.CharField(label='Something Alive (Plural)', max_length=20, required=True)
    ml3var19 = forms.CharField(label='Adverb', max_length=20, required=True)
    ml3var20 = forms.CharField(label='Noun', max_length=20, required=True)
   
    
    # madlib2_email = forms.EmailField(required=True)
    # content = forms.CharField(required=True, widget=forms.Textarea)
    