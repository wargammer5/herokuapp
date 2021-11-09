from django.db import models

# Create your models here.



class TypeDonaite(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    number_user = models.CharField(max_length=50, verbose_name='Телефон')

    def __str__(self):
        return self.name