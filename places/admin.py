from django.contrib import admin
from .models import Place, Image
from django.utils.safestring import mark_safe


class ImageEdit(admin.TabularInline):
    model = Image
    readonly_fields = ['get_preview']
    def get_preview(self, obj):
        return mark_safe(
            '<img src="{url}" height=200 />'.format(
                url=obj.image.url,
            )
        )


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'place')

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    #readonly_fields = ['get_preview']
    list_display = ('id', 'title',)
    inlines = [ImageEdit,]



#admin.site.register(Place, PlaceAdmin)
#admin.site.register(Image, ImageAdmin)

