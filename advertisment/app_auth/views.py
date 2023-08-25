from django.shortcuts import render
from django.urls import reverse
from django.contrlib.auth import authemticate, login, logout

def login_view(request):
    pass
def profile_view(request):
    return render(request, 'app_auth/profile.html') 

def logout_view(request):
    pass