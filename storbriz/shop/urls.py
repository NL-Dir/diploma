from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import GoodsList, GoodDetailView, CartDetailView, delete_from_cart, add_to_cart

app_name = 'shop'

urlpatterns = [
    path('', GoodsList.as_view(), name='home'),
    path('good/<int:pk>', GoodDetailView.as_view(), name='good'),
    path('<int:pk>/cart', CartDetailView.as_view(), name='cart'),
    path('<int:pk>/cart/<int:good_id>/delete', delete_from_cart, name='delete_from_cart'),
    path('<int:pk>/cart/<int:good_id>/add', add_to_cart, name='add_to_cart'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
