from django.db import models

class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    text = models.TextField('Текст')
    date = models.DateTimeField('Дата')

    def __str__(self):
        return self.title
