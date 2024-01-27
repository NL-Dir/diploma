from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import GoodsList, GoodDetailView

app_name = 'shop'

urlpatterns = [
    path('', GoodsList.as_view(), name='home'),
    path('good/<int:pk>', GoodDetailView.as_view(), name='good'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
