from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import GoodsFilteredList, GoodDetailView, CartDetailView, delete_from_cart, add_to_cart, OrderCreateView, \
    GoodsList, GoodsSearchList, QuestionCreateView

app_name = 'shop'


urlpatterns = [
    path('', GoodsList.as_view(), name='home'),
    path('category/<int:pk>', GoodsFilteredList.as_view(), name='category'),
    path('search', GoodsSearchList.as_view(), name='search'),
    path('good/<int:pk>', GoodDetailView.as_view(), name='good'),
    path('cart/<int:pk>', CartDetailView.as_view(), name='cart'),
    path('<int:pk>/cart/<int:good_id>/delete', delete_from_cart, name='delete_from_cart'),
    path('<int:pk>/cart/<int:good_id>/add', add_to_cart, name='add_to_cart'),
    path('order', OrderCreateView.as_view(), name='order'),
    path('support', QuestionCreateView.as_view(), name='support'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
