from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Good


class GoodsList(ListView):
    model = Good
    template_name = 'src/home.html'
    context_object_name = 'goods'

    def get_queryset(self):
        queryset = {'new_goods': Good.objects.order_by('is_new', 'id'),
                    'top_goods': Good.objects.filter(is_popular=True)}
        return queryset


class GoodDetailView(DetailView):
    model = Good
    template_name = 'src/page-product.html'
    context_object_name = 'good'
