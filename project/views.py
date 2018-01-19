from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt

# Create your views here.
def Welcome(request):
    return render(request, 'welcome.html')

def pictures_today(request):
    date = dt.date.today()
    return render(request, 'all-news/today-pictures.html', {"date": date,})

# View Function to present news from past days
def past_days_pictures(request, past_date):

    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(news_today)

    return render(request, 'all-news/past-pictures.html', {"date": date})

def news_of_day(request):
    date = dt.date.today()

    # FUNCTION TO CONVERT DATE OBJECT TO FIND EXACT DAY
    day = convert_dates(date)
    html = f'''
        <html>
            <body>
                <h1>News for {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)
