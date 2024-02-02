from django.contrib import admin

from .models import Cart, Order, Good, CartGood


class GoodAdmin(admin.ModelAdmin):
    list_display = ['article', 'name', 'color', 'price']


admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Good, GoodAdmin)
admin.site.register(CartGood)
