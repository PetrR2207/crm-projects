from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request, 'crmsystem/home.html')