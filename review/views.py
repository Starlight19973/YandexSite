from django.shortcuts import render
from .models import Review

def review_home(request):
    reviews = Review.objects.all()
    return render(request, 'review/review_home.html', {'reviews': reviews})

