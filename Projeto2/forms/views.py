from django.shortcuts import render
from datetime import datetime
from forms.aux_funct import *

# Create your views here.


def home(request):
    tparams = {
        'title': 'Home Page',
        'year': datetime.now().year,
    }

    return render(request, 'index.html', tparams)


def contact(request):
    tparams = {
        'title': 'Our team',
        'year': datetime.now().year,
    }
    return render(request, 'contact.html', tparams)


def about(request):
    tparams = {
        'year': datetime.now().year,
    }
    return render(request, 'about.html', tparams)

def movies(request):
    tparams = {'films': listMovies()}
    return render(request, 'movies.html', tparams)

def movie_info(request):
    tparams = info(request.GET['mov'])
    return render(request, 'movie_info.html', tparams)