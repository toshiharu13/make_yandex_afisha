from django.db import models

class Place(models.Model):
    title = models.CharField('Название', max_length=100)
    description_short = models.TextField('Короткое описание', blank=True)
    description_long = models.TextField('Полное описание')
    lng = models.FloatField('Долгота')
    lat = models.FloatField('Широта')

    def __str__(self):
        return self.title

class Image(models.Model):
    title = models.CharField(max_length=100)
    number = models.IntegerField()
    image = models.ImageField(upload_to='place_images')

    def __str__(self):
        return f'{self.number} {self.title}'

    class Meta:
        ordering = ['title', 'number']
