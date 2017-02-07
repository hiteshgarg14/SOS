import json
from django.shortcuts import render, redirect
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import NonUserContactForm, ReportOnceForm, IExperienceForm, ProfileOverviewForm, \
                    UserOverviewForm, ProfileContactForm, UserContactForm, ProfileProfessionalForm
from utils import send_twilio_message
from .models import ProfileModel
from django.core.urlresolvers import reverse

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
    try:
        puser = ProfileModel.objects.get(user=request.user)
    except:
        puser = ProfileModel.objects.create(user=request.user)

    if request.method == 'POST':
        p_overform = ProfileOverviewForm(data=request.POST, instance=request.user.profilemodel)
        u_overform = UserOverviewForm(data=request.POST, instance=request.user)
        p_contactform = ProfileContactForm(data=request.POST, instance=request.user.profilemodel)
        u_contactform = UserContactForm(data=request.POST, instance=request.user)
        p_pform = ProfileProfessionalForm(data=request.POST, instance=request.user.profilemodel)
        if p_overform.is_valid() and u_overform.is_valid() and p_contactform.is_valid() \
            and u_contactform.is_valid() and p_pform.is_valid():
                p_overform.save()
                u_overform.save()
                p_contactform.save()
                u_contactform.save()
                p_pform.save()
                msg = 'Profile updated Successfully'
                return HttpResponseRedirect('/profile/')
        else:
            print "Errors"
            print p_overform.errors
            print u_overform.errors
            print p_contactform.errors
            print u_contactform.errors
            print p_pform.errors
    else:
        p_overform = ProfileOverviewForm(instance=request.user.profilemodel)
        u_overform = UserOverviewForm(instance=request.user)
        p_contactform = ProfileContactForm(instance=request.user.profilemodel)
        u_contactform = UserContactForm(instance=request.user)
        p_pform = ProfileProfessionalForm(instance=request.user.profilemodel)
    context = {'p_overform':p_overform, 'u_overform':u_overform, 'p_contactform':p_contactform,
               'u_contactform':u_contactform, 'p_pform':p_pform }
    return render(request,'sosapp/profile.html', context)


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

def chatIndex(request):
    return render(request,'sosapp/firechat/index.html')

def education(request):
    return render(request, 'sosapp/blog-single.html')
