from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import NonUserContactForm

def index(request):
    contact_form = NonUserContactForm(request.POST or None)
    if request.method == 'POST':
        if contact_form.is_valid():
            contact_form.save()
            return HttpResponseRedirect('/')
        return render(request,'sosapp/index-default.html',{'contact_form':contact_form})
    return render(request,'sosapp/index-default.html',{'contact_form':contact_form})

@login_required
def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/')
