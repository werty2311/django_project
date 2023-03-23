from django.urls import path, include

from . import views
urlpatterns = [
    path('', views.news_main, name='news_main'),
    path('create_news', views.create_news, name = 'create_news')
    ]
