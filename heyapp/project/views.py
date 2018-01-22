from .models import photos
from django.shortcuts import render,redirect
from django.http import HttpResponse
import datetime as dt

# Create your views here.
def pictures_today(request):
    project = photos.objects.all()
    return render(request, 'today-pictures.html', {"photos": project})
