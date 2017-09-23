from django.shortcuts import render
from django.http import HttpResponse
import os
from .models import Post
from django.utils import timezone


def index(request):
    return HttpResponse("Hello world! This is our second view.")


def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'teste/post_list.html', {'posts': posts})


def teste(request):
	return render(request, 'teste/teste.html', {})


	