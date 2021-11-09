from django.db import models

# Create your models here.


class Status(models.Model):
    nameStatus = models.CharField(max_length=255 , verbose_name='Название статуса')
    logo = models.ImageField(upload_to='about_us/logoStatus/', verbose_name='Логотип')
    description = models.TextField(verbose_name='Описания цели')

    def __str__(self):
        return self.name_status


class TeamOfHebron(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    lastName = models.CharField(max_length=255, verbose_name='Фамилия')
    image = models.ImageField(upload_to='about_us/photoTeam/')
    post = models.TextField( verbose_name='Должность')

    def __str__(self):
        return self.name + ' ' + self.last_name


class Gallery(models.Model):
    altPhoto = models.CharField(max_length=255, verbose_name='Описание фото') 
    photo = models.ImageField(upload_to='about_us/gallery/')


    def __str__(self):
        return self.alt_photo


class Video(models.Model):
    video = models.FileField(upload_to='about_us/video/')



class FAQ(models.Model):
    question = models.CharField(max_length=255, verbose_name='Вопрос')
    answer = models.TextField(verbose_name='Ответ на вопрос')

    def __str__(self):
        return self.question