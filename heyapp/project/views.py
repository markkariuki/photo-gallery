from .models import photos
from django.shortcuts import render,redirect
from django.http import HttpResponse
import datetime as dt

# Create your views here.
def pictures_today(request):
    date = dt.date.today()
    project = photos.objects.all()
    return render(request, 'all-pics/today-pictures.html', {"date": date,"project":project})
