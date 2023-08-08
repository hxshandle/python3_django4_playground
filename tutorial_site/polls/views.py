from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, Polls")

def home(request):
    return HttpResponse("This is the Polls home page")