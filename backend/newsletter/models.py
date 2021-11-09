from django.db import models

# Create your models here.


class NewLetter(models.Model):
    photo = models.ImageField(upload_to = 'news/images/')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.TextField(verbose_name="Описание")
    CHOISEN_NEWSLETTER = [
        ('Н', 'Новости'), 
        ('У', 'Истории успеха'),
        ('Б', 'Блог'),
    ]
    choiseTypeNews = models.CharField(max_length= 1, choices=CHOISEN_NEWSLETTER, verbose_name='Тип Новостей')

    def __str__(self):
        return self.title
