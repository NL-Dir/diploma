from django.shortcuts import render
from django.views.generic import ListView

from .models import Good


class GoodsList(ListView):
    model = Good
    template_name = 'src/home.html'
    context_object_name = 'goods'
    queryset = Good.objects.order_by('id')
