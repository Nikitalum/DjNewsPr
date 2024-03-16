from django.db import models

class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    text = models.TextField('Текст')
    date = models.DateTimeField('Дата')

    def __str__(self):
        return f'{self.title},{self.date},{self.text}'
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
