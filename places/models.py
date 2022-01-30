from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Название', max_length=100)
    description_short = models.TextField('Короткое описание', blank=True)
    description_long = HTMLField('Полное описание', blank=True)
    lng = models.FloatField('Долгота')
    lat = models.FloatField('Широта')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['pk']

class Image(models.Model):
    title = models.CharField(max_length=100, blank=True)
    number = models.IntegerField(default=0)
    image = models.ImageField(upload_to='place_images')
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='images')

    @property
    def get_absolute_image_url(self):
        return self.image.url

    def __str__(self):
        return f'{self.get_absolute_image_url}'

    class Meta:
        ordering = ['title', 'number']
