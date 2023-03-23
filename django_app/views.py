from django.shortcuts import render
from news.models import Articles


def home(request):
    data = {
        'title': 'Главная страница',
    }
    return render(request, 'django_app/home.html', data)


def solar_system(request):
    return render(request, 'django_app/solar_system.html',  {'title': 'Солнечная система'})


def galaxies(request):
    return render(request, 'django_app/galaxies.html', {'title': 'Галактики'})


def missions(request):
    return render(request, 'django_app/missions.html', {'title': 'Космические миссии'})


def news(request):
    news = Articles.objects.all().values('title', 'intro', 'date', 'id')
    return render(request, 'django_app/news.html', {'title': 'Новости', 'news': news})


def shop(request):
    return render(request, 'django_app/shop.html', {'title': 'Магазин'})


def replies(request):
    return render(request, 'django_app/replies.html', {'title': 'Отзывы'})

