from django.db import models

class Place(models.Model):
    title = models.CharField('Название', max_length=100)
    description_short = models.TextField('Короткое описание', blank=True)
    description_long = models.TextField('Полное описание')
    image = models.ImageField('Изображение', null=True, blank=True)
    lng = models.FloatField('Долгота')
    lat = models.FloatField('Широта')

    def __str__(self):
        return self.title