from django import utils
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    father_name = models.CharField(verbose_name="Отчество", max_length=100, null=True)
    company_name = models.CharField(verbose_name="Название компании", max_length=100, null=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Gruz(models.Model):
    user_id = models.IntegerField(verbose_name="ID клиента", null=True)
    name = models.CharField(verbose_name="Название груза", max_length=100, null=True)
    manufacture_time = models.DateTimeField(verbose_name="Время отправки заявки", null=True, default=utils.timezone.now)
    sent_to_position_date = models.DateField(verbose_name="Время отправки на место назначения", null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Груз'
        verbose_name_plural = 'Грузы'
