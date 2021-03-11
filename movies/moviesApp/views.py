from django.shortcuts import render
from .models import Movie
from django.core.paginator import Paginator

# Create your views here.

def getAllMovies(request):
    movies = Movie.objects.all()
    movieName = request.GET.get("name")
    if movieName != '' and movieName is not None:
        movies = movies.filter(name__icontains=movieName)
    paginator = Paginator(movies, 2)
    page = request.GET.get('page')
    movies = paginator.get_page(page)
    return render(request, "moviesApp/index.html", context={'movies': movies})