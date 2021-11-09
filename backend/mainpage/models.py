from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    lastname = models.CharField(max_length=100, verbose_name='Фамилия')
    email = models.EmailField(max_length=255 , verbose_name='Email', unique=True)
    password = models.CharField(max_length=50, verbose_name='Пароль')
    verificPassword = models.CharField(max_length=50, verbose_name='Проверочный пароль')

    def __str__(self):
        return self.email





class Comment(models.Model):
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    description = models.TextField(verbose_name="Коментарий")

    def __str__(self):
        return self.user



class TypesOfDonations(models.Model):
    logo = models.ImageField(upload_to='headerPage/logo/')
    