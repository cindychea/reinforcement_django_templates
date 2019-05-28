from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def root(request):
    return HttpResponseRedirect('profiles/new')

def new_profile(request):
    context = {
        'element': ['email', 'username', 'pin', 'website', 'address', 'alias']
    }
    return HttpResponse(render(request, 'profiles/new.html', context))