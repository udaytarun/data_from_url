from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def data_from_url(request,name):
    return HttpResponse(f'HII {name} I AM BATMAN')
