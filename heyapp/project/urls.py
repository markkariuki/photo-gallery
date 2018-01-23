from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.pictures_today, name='picturesToday'),
    url(r'^photo/(\d+)', views.single_photo, name='singlePhoto'),
    url(r'^search/', views.search_results, name='search_results')
]
