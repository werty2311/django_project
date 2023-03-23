from django.shortcuts import render, redirect
from .models import Replies
from .forms import ReplisForm


def replies_main(request):
    replies = Replies.objects.order_by('-date')
    return render(request, 'replies/replies_main.html', {'replies' : replies})


def create_reply(request):
    error = ''
    if request.method == 'POST':
        form = ReplisForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('replies_main')
        else:
            error = 'Форма была отправлена неверной'
    form = ReplisForm()

    data = {
        'form' : form,
        'error' : error
    }
    return render(request, 'replies/create_reply.html', data)
