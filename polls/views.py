from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request) :
    return HttpResponse("hello you're ate the polls index.")