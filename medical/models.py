from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=250, verbose_name='Услуга')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    picture = models.ImageField(upload_to='service/photo', blank=True, null=True, verbose_name='Фото')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class Doctor(models.Model):
    name = models.CharField(max_length=250, verbose_name='Имя')
    surname = models.CharField(max_length=250, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=250, verbose_name='Отчество')
    job_title = models.CharField(max_length=250, verbose_name='Должность')
    photo = models.ImageField(upload_to='doctors/photo', blank=True, null=True, verbose_name='Фото')

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic}'

    class Meta:
        verbose_name = 'Врач'
        verbose_name_plural = 'Врачи'
