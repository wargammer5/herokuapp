from django.db import models

# Create your models here.

class SucceesStories(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    lastName = models.CharField(max_length=100, verbose_name='Фамилия')
    image = models.ImageField(upload_to='stadies/photoSuccess/')
    description = models.TextField(verbose_name='Описание успеха')

    def __str__(self):
        return self.name



class OtherSuccessStories(models.Model):
    pib = models.CharField(max_length=255, verbose_name='P.I.B')
    numberTelephon = models.CharField(max_length=50, verbose_name='Номер телефона')
    email = models.EmailField(max_length=255, unique=True, verbose_name='Email')
    description = models.TextField(verbose_name='История успеха')

    def __str__(self):
        return self.pib


