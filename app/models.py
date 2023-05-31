from django.db import models
from django.contrib.auth.models import User

class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Водитель', null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Ф.И.О')
    license_front = models.ImageField(null=True, upload_to='licenses_front/')
    license_back = models.ImageField(null=True, upload_to='licenses_back/')
    phone_number = models.CharField(max_length=20, verbose_name='Контактный номер', blank=True)
    email = models.EmailField(verbose_name='Электронная почта', null=True, blank=True)

    class Meta:
        verbose_name = 'Водитель'
        verbose_name_plural = 'Водители'


class Truck(models.Model):
    driver = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='trucks/', null=True)
    plate_number = models.CharField(max_length=20, verbose_name='Номерной знак')
    model = models.CharField(max_length=255, verbose_name='Модель')
    capacity = models.FloatField(verbose_name='Ёмкость')


    class Meta:
        verbose_name = 'Грузовик'
        verbose_name_plural = 'Грузовики'

    def __str__(self) -> str:
        return self.model

class Shipment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255, verbose_name='Описание')
    phone_number = models.CharField(max_length=15, verbose_name='Контактный номер', null=True)
    origin = models.CharField(max_length=255, verbose_name='Начало')
    destination = models.CharField(max_length=255, verbose_name='Место назначения')
    weight = models.FloatField(verbose_name='Масса')
    status = models.CharField(max_length=20, default='pending', verbose_name='Статус')
    assigned_truck = models.ForeignKey(Truck, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_shipments', verbose_name='Назначенный Грузовик')


    class Meta:
        verbose_name = 'Отгрузка'
        verbose_name_plural = 'Отгрузки'

    def __str__(self) -> str:
        return self.origin

