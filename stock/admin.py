from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Stock, Profile, Provider, Buyer, WriteOff, Procurement

admin.site.register(Profile)
admin.site.register(Provider)
admin.site.register(Buyer)
admin.site.register(WriteOff)
admin.site.register(Procurement)


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ['id', 'article', 'name', 'miniature', 'description', 'country', 'net_weight',
                    'gross_weight', 'price', 'client_price', 'count']

    readonly_fields = ["miniature"]

    def miniature(self, obj):
        return mark_safe(f'<img src="{obj.photo.url}">')
