from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def srujana(request):
    return HttpResponse('<marquee><h1>Srujana tinavara, Era vadilestunava.....</h1></maquee>')

def meghana(request):
    return HttpResponse('<marquee><i>My name is meghana sirrr....</i></marquee>')