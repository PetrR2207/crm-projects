from django.shortcuts import render
from django.http import HttpResponse

def finance(request):
    return render(request, 'finance/finance.html')