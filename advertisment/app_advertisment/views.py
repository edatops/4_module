from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'app_advertisement/index.html')

def top_sellers(request):
    return render(request, 'app_advertisement/top-sellers.html')