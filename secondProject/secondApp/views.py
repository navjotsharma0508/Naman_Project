from django.shortcuts import render
from django.http import HttpResponse
import datetime

def currentTime1(request):
    date=datetime.datetime.now()
    msg='<h1> Hello Good Evening </h1></hr>'
    msg1=msg+'<h1>Now server time is '+str(date)+'</h1>'
    return HttpResponse(msg1)

# Create your views here.
