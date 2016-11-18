from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request,'sosapp/index-default.html',{})

@login_required
def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/')
