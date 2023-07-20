from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from django.template import loader

def home(request):
    template = loader.get_template('client/home.html')
    return HttpResponse(template.render())
