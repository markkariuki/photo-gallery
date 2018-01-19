from .models import photos
from django.shortcuts import render,redirect
from django.http import HttpResponse
import datetime as dt

# Create your views here.
def Welcome(request):
    return render(request, 'welcome.html')

def pictures_of_day(request):
    project = photos.todays_project()
    return render(request, 'all-pics/today-pictures.html')

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

    return render(request, 'all-pics/past-pictures.html', {"date": date})
