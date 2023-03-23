from django.urls import path
from . import views
urlpatterns = [
    path('home', views.home, name='home'),
    path('solar_system', views.solar_system,  name='solar_system'),
    path('galaxies', views.galaxies,  name='galaxies'),
    path('missions', views.missions,  name='missions'),
    path('news', views.news,  name='news'),
    path('shop', views.shop,  name='shop'),
    path('replies', views.replies, name = 'replies')
    ]
