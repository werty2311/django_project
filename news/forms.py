from .models import Articles
from django.forms import ModelForm, TextInput, DateInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'intro', 'text', 'date']

        widgets = {
            "title" : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Название статьи'
            }),
            "intro": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи'
            }),

            "date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации'
            }),

            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи'
            })
        }