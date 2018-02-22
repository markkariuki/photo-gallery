from .models import photos
from django.shortcuts import render,redirect
from django.http import HttpResponse
import datetime as dt

# Create your views here.
def pictures_today(request):
    project = photos.objects.all()
    return render(request, 'today-pictures.html', {"photos": project})

def single_photo(request, photo_id):
    photo = photos.objects.get(id=photo_id)
    return render(request, 'photos.html', {'photo':photo})

def search_results(request):

    if 'photo' in request.GET and request.GET["photo"]:
        search_term = request.GET.get("photo")
        searched_photos = photos.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"photos": searched_photos})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
