from django.contrib.auth.models import User
from django.db import models

from transport.models import Transport

# Create your models here.

class Schedule(models.Model):
    BLUE = 'blue'
    RED = 'red'
    PINK = 'pink'
    GREEN = 'green'
    STATUS_COLORS = [
        (BLUE, 'Синий - Подтвержден'),
        (RED, 'Красный - Срочно'),
        (PINK, 'Розовый - Не подтвержден'),
        (GREEN, 'Зеленый - Завершен/Выполнен')  #описание цветов в расписании
    ]
    status = models.CharField(choices=STATUS_COLORS, max_length=35, default=PINK)
    object_name = models.CharField(max_length=150) # название обьекта
    body_object = models.TextField() # описание обьекта
    transport_name = models.ForeignKey(Transport, models.SET_NULL, null=True, blank=True) # авто, которое поедет на выезд
    created_at = models.DateTimeField(auto_now_add=True) # дата создания(не факт что нужно)
    departure_date = models.DateField()
    departure_date_end = models.DateField(null=True, blank=True)
    team = models.ManyToManyField('accounts.Worker', blank=True, related_name='schedules') #ключ к Юзеру
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    uuid = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f'{self.object_name}, {self.departure_date}'



