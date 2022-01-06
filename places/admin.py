from django.contrib import admin
from .models import Place, Image


#class ImageAdmin(Images):


admin.site.register(Place)
admin.site.register(Image)

