# Generated by Django 3.2.7 on 2021-09-29 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OtherSuccessStories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pib', models.CharField(max_length=255, verbose_name='P.I.B')),
                ('numberTelephon', models.CharField(max_length=50, verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email')),
                ('description', models.TextField(verbose_name='История успеха')),
            ],
        ),
        migrations.CreateModel(
            name='SucceesStories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('lastName', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('image', models.ImageField(upload_to='stadies/photoSuccess/')),
                ('description', models.TextField(verbose_name='Описание успеха')),
            ],
        ),
    ]
