from django.contrib import admin
from .models import Place, Image


class ImageEdit(admin.TabularInline):
    model = Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'place')

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    inlines = [ImageEdit,]


#admin.site.register(Place, PlaceAdmin)
#admin.site.register(Image, ImageAdmin)

