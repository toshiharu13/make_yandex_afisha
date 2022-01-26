from django.contrib import admin
from .models import Place, Image
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableAdminMixin
from adminsortable2.admin import SortableInlineAdminMixin


class ImageEdit(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    readonly_fields = ['get_preview']

    def get_preview(self, obj):
        return mark_safe(
            '<img src="{url}" height=200 />'.format(
                url=obj.image.url,
            )
        )
    extra = 0


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'title', 'place')


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    inlines = [ImageEdit,]


