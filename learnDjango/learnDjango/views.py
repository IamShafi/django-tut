from django.shortcuts import render
from django.http import HttpResponse

def Home(request):
    return HttpResponse("Homepage")

def About(request):
    return HttpResponse("About Page")