from .models import photos
from django.shortcuts import render,redirect
from django.http import HttpResponse
import datetime as dt

# Create your views here.


def allphotos(request):
    photos = Photos.objects.all()
    return render(request, 'today-pictures.html', {'photos':photos})

# View Function to present news from past days
def past_days_pictures(request,past_date):

    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(pictures_today)

    project = photos.days_pictures(date)
    return render(request, 'all-pics/today-pictures.html', {"date": date})

def pictures_today(request):
    date = dt.date.today()
    project = photos.todays_pictures()
    return render(request, 'all-pics/today-pictures.html', {"date": date,"project":project})
