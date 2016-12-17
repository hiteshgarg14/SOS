import json
from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import NonUserContactForm


def index( request ):
    if request.method == 'POST':
    	return contactUsSaveService( request );
    return render(request,'sosapp/index-default.html',{"contact_form":None})
   	
def contactUsSaveService( request ):
    contact_form = NonUserContactForm( request.POST or None )
    if contact_form.is_valid():
        contact_form.save()
        return JsonResponse({ "status": 1, "message" : "Thank you! We will connect to you soon !" })
    return JsonResponse({ "status": 0, "message": "422 Unprocessable Entity", "errors" : []  },status=422)

@login_required
def logout( request ):
	auth.logout(request)
	return HttpResponseRedirect('/')