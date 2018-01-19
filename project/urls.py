from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.Welcome,name = 'Welcome'),
    url('^today/$',views.pictures_of_day,name='picturesToday'),
    url(r'^archives/\d{4}-\d{2}-\d{2}/$',views.past_days_pictures,name = 'pastPictures')
]
