from django.shortcuts import render
from django.views.generic import ListView

from .models import Good


class GoodsList(ListView):
    model = Good
    template_name = 'src/home.html'
    context_object_name = 'goods'

    def get_queryset(self):
        queryset = {'new_goods': Good.objects.all(),
                    'top_goods': Good.objects.all()}
        return queryset

