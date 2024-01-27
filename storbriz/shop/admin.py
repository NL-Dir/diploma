from django.contrib import admin

from .models import Person, Cart, Order, Good


class GoodAdmin(admin.ModelAdmin):
    list_display = ['article', 'name', 'color', 'price']


admin.site.register(Person)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Good, GoodAdmin)
