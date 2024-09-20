from django.contrib.auth.models import AbstractUser
from django.db import models

from medical.models import Doctor, Service


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Почта')

    first_name = models.CharField(max_length=150, verbose_name='Имя')

    last_name = models.CharField(max_length=150, verbose_name='Фамилия')

    avatar = models.ImageField(upload_to='users/photo', verbose_name='Аватар', blank=True, null=True,
                               help_text='Загрузите свой аватар')
    phone = models.CharField(max_length=35, verbose_name='Номер телефона', blank=True,
                             null=True, help_text='Введите номер телефона')
    city = models.CharField(max_length=35, verbose_name='Город', blank=True,
                            null=True, help_text='Введите город')
    token = models.CharField(max_length=100, verbose_name='Токен', blank=True, null=True, )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Record(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="Услуги")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="Доктор")
    created_at = models.DateTimeField(auto_now_add=True)
    record_time = models.DateField(verbose_name='Дата записи')
    diagnosis = models.CharField(max_length=300, blank=True, null=True, verbose_name='Диагноз')
    is_active = models.BooleanField(default=True, verbose_name='Отмена записи')

    def __str__(self):
        return f"{self.user} записан на {self.service.name} к {self.doctor}."

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
        permissions = [
            ('can_add_record', 'Может добавлять запись'),
            ('can_change_record', 'Может изменять запись'),
            ('can_view_record', 'Может просматривать запись'),
            ('can_delete_record', 'Может удалять запись'),
        ]
