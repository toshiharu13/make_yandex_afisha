from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from .models import Image, Place


class ImageEdit(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    readonly_fields = ['get_preview']

    def get_preview(self, obj):
        return format_html('<img src= {} height=200 />',
                mark_safe(obj.image.url))


    extra = 0


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'title', 'place')
    raw_id_fields = ('place',)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    inlines = [ImageEdit]
