from django.urls import path, include

from . import views
urlpatterns = [
    path('', views.replies_main, name='replies_main'),
    path('create_reply', views.create_reply, name = 'create_reply')
    ]
