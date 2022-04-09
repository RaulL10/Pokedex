from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Hello!</h1>')

def about(request):
    return HttpResponse('<h1>This is About</h1>')

def index(request):
    return HttpResponse('<h1>All Pokemon</h1>')