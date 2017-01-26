import json
from django.shortcuts import render, redirect
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import NonUserContactForm, ReportOnceForm, IExperienceForm
from utils import send_twilio_message

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


@login_required
def profile( request ):
    # auth.logout(request)
    return render(request,'sosapp/profile.html')
    

@login_required
def report_once(request):
    r_form = ReportOnceForm(request.POST or None)
    if r_form.is_valid():
        tmp = r_form.save(commit=False)
        tmp.r_user = request.user
        r_form.save()
        body = 'Hi {0}! Thanks For Your Story.'.format(request.user)
        sent = send_twilio_message('+917597004257',body)
        #print sent.sid
        # Imporvement Needed!
        return redirect('sos:index')
    return render(request,'sosapp/report_once.html',{'form':r_form})

@login_required
def i_experienced(request):
    i_form = IExperienceForm(request.POST or None)
    if i_form.is_valid():
        tmp = i_form.save(commit=False)
        tmp.i_user = request.user 
        i_form.save()
        body = 'Hi {0}! Thanks For Your Story.'.format(request.user)
        sent = send_twilio_message('+917597004257',body)
        #print sent.sid
        # Imporvement Needed!
        return redirect('sos:index') 
    return render(request,'sosapp/i_experienced.html',{'form':i_form})     