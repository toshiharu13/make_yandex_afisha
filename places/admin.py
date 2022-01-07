from django.contrib import admin
from .models import Place, Image


class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'place')


class PlaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)


admin.site.register(Place, PlaceAdmin)
admin.site.register(Image, ImageAdmin)

