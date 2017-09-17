from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world! This is our second view.")
# Create your views here.
