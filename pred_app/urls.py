from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [

    path('Home', views.Home, name='Home'),
    path('index', views.index, name='index'),
    path('pred', views.pred, name='pred'),
    path('baseN', views.baseN, name="baseN"),
    path('news.html', views.news, name="news"),
    url(r'', include('contact.urls')),
]