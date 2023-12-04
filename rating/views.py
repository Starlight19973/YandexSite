from django.shortcuts import render
from .models import Article



def rating_home(request):
    rating = Article.objects.all()
    return render(request, 'rating/rating_home.html', {'rating': rating})
