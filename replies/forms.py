from .models import Replies
from django.forms import ModelForm, TextInput, EmailInput, DateInput, Textarea, TimeInput


class ReplisForm(ModelForm):
    class Meta:
        model = Replies
        fields = ['title', 'text', 'email', 'date', 'time']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Отзыв'
            }),

            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Содержание'
            }),

            "email": EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Элпочта'
            }),

            "date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата отзыва'
            }),

            "time": TimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Время отзыва'
            })

        }
