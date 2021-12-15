from django.db import models
from django.contrib.auth.models import User


class Place(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название места')
    discription = models.TextField(blank=True, verbose_name='Описание места')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.title

