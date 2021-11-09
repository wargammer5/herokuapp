from django.db import models

# Create your models here.


class FormDonaite(models.Model):
    COAT = [    ('1','500'),
                ('2','1000'),
                ('3','1500')    
    ]

    WAY_OF_WRITING = [
        ('м','Каждый месяц'),
        ('к','Каждый квартал')
    ]

    coat = models.CharField(max_length=10, choices=COAT, verbose_name='Сумма')
    way_of_writing = models.CharField(max_length=10 , choices=WAY_OF_WRITING, verbose_name='Способ спесания', blank=True)
    pib = models.CharField(max_length=255, verbose_name='П.I.Б')
    email = models.EmailField(max_length=255, verbose_name='Email') 


    def __str__(self):
        return self.pib



