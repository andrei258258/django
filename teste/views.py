from django.shortcuts import render
from django.http import HttpResponse
import os

def index(request):
    return HttpResponse("Hello world! This is our second view.")


def post_list(request):
	return render(request, 'teste/post_list.html', {})


def teste(request):
	return render(request, 'teste/teste.html', {})


	