from django.db import models


class Articles(models.Model):
    title = models.CharField('Название', max_length=150)
    intro = models.CharField('Анонс', max_length=350)
    text = models.TextField('Содержание')
    date = models.DateField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'