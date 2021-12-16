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
        return self.short_title()

    def short_title(self):
        if len(self.title) < 30:
            return self.title
        else:
            return self.title[:30] + '...'

    def short_discription(self):
        if len(self.discription) < 30:
            return self.discription
        else:
            return self.discription[:30] + '...'
