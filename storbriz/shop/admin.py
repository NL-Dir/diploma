from django.contrib import admin

from .models import Person, Cart, Order, Good

admin.site.register(Person)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Good)

# Register your models here.
