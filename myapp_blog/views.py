from django.shortcuts import render
from django.http import HttpResponse
from .models import Tour

# Create your views here.
def home(request):
    tours = Tour.objects.all()
    context = {
        'tours': tours
    }
    return render(request, 'myapp_blog/index.html', context)



