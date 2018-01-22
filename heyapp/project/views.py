from .models import photos
from django.shortcuts import render,redirect
from django.http import HttpResponse
import datetime as dt

# Create your views here.



# View Function to present news from past days

def pictures_today(request):
    date = dt.date.today()
    photos = photos.objects.all()
    return render(request, 'all-pics/today-pictures.html', {"photos": photos})
