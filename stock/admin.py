from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Stock



@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ['id', 'article', 'name', 'miniature', 'description', 'country', 'net_weight',
                    'gross_weight', 'price']

    readonly_fields = ["miniature"]

    def miniature(self,obj):
        return mark_safe(f'<img src="{obj.photo.url}">')