# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    response = "Hello, I am your first request!"
    return HttpResponse(response, 'Hello World!')

def new(request):
    pass

def create(request):
    pass

def logout(request):
    pass