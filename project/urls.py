from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.Welcome,name = 'Welcome'),
    url('^today/$',views.pictures_of_day,name='picturesToday')
]
