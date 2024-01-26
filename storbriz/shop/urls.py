from django.contrib import admin
from django.urls import path

from .views import GoodsList

app_name = 'shop'

urlpatterns = [
    path('', GoodsList.as_view(), name='home'),
]
