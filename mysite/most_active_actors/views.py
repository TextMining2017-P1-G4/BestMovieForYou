from django.conf import settings
from django.shortcuts import render
from django.template import loader

# Create your views here.

def index(request):

    context = {}
    
    return render(request, 'most_active_actors/index.html', context)