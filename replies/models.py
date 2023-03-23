from django.db import models

class Replies(models.Model):
    title = models.CharField('Отзыв', max_length=150)
    email = models.EmailField('Эл.почта', max_length=350)
    text = models.TextField('Содержание')
    date = models.DateField('Дата отзыва')
    time = models.TimeField('Время отзыва')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
