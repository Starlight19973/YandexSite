from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

# Ваши существующие представления

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')






