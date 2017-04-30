from django.shortcuts import render, redirect
from collection.forms import madlib2Form
from django.http import HttpResponseRedirect


# Create your views here.

def index(request): 
    # defining the variable
    number = 6
    # passing the variable to the view
    return render(request, 'index.html', {
        'number': number,
    })
    
def madlib2(request):
    form_class = madlib2Form
    
    if request.method == 'POST':
        form = form_class(data=request.POST)
        
        if form.is_valid():
            request.session['var1'] = request.POST.get('var1', '')
            request.session['var2'] = request.POST.get('var2', '')
            request.session['var3'] = request.POST.get('var3', '')
            request.session['var4'] = request.POST.get('var4', '')
            request.session['var5'] = request.POST.get('var5', '')
            request.session['var6'] = request.POST.get('var6', '')
            request.session['var7'] = request.POST.get('var7', '')
            request.session['var8'] = request.POST.get('var8', '')
            request.session['var9'] = request.POST.get('var9', '')
            request.session['var10'] = request.POST.get('var10', '')
            request.session['var11'] = request.POST.get('var11', '')
            request.session['var12'] = request.POST.get('var12', '')
            request.session['var13'] = request.POST.get('var13', '')
            request.session['var14'] = request.POST.get('var14', '')
            request.session['var15'] = request.POST.get('var15', '')
            request.session['var16'] = request.POST.get('var16', '')
            request.session['var17'] = request.POST.get('var17', '')
            request.session['var18'] = request.POST.get('var18', '')
            request.session['var19'] = request.POST.get('var19', '')
            request.session['var20'] = request.POST.get('var20', '')
            request.session['var21'] = request.POST.get('var21', '')
            request.session['var22'] = request.POST.get('var22', '')
            request.session['var23'] = request.POST.get('var23', '')
        
            
            return HttpResponseRedirect('madlib2Filled/')
    else:
        form =madlib2Form()
    
    return render(request, 'madlib2.html', {'form': form_class,})
    
def madlib2Filled(request): 
    # defining the variable
    var1 =  request.session['var1']
    var2 =  request.session['var2']
    var3 =  request.session['var3']
    var4 =  request.session['var4']
    var5 =  request.session['var5']
    var6 =  request.session['var6']
    var7 =  request.session['var7']
    var8 =  request.session['var8']
    var9 =  request.session['var9']
    var10 =  request.session['var10']
    var11 =  request.session['var11']
    var12 =  request.session['var12']
    var13 =  request.session['var13']
    var14 =  request.session['var14']
    var15 =  request.session['var15']
    var16 =  request.session['var16']
    var17 =  request.session['var17']
    var18 =  request.session['var18']
    var19 =  request.session['var19']
    var20 =  request.session['var20']
    var21 =  request.session['var21']
    var22 =  request.session['var22']
    var23 =  request.session['var23']
    
    # passing the variable to the view
    return render(request, 'madlib2Filled.html', {
        'var1': var1, 'var2': var2, 'var3': var3, 'var4': var4,
        'var5': var5, 'var6': var6, 'var7': var7, 'var8': var8,
        'var9': var9, 'var10': var10, 'var11': var11, 'var12': var12,
        'var13': var13, 'var14': var14, 'var15': var15, 'var16': var16,
        'var17': var17, 'var18': var18, 'var19': var19, 'var20': var20,
        'var21': var21, 'var22': var22, 'var23': var23,
    })