from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.forms import modelformset_factory
from django.urls import reverse, reverse_lazy

from .models import Good, Cart


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


class CartDetailView(DetailView):
    model = Cart
    template_name = 'src/basket.html'
    context_object_name = 'cart'

    def get_success_url(self, request):
        if 'delete_from_cart' in self.request.POST:
            request.user.cart.goods.remove(request.POST['good_id'])
            return reverse_lazy('shop:cart',
                                kwargs={'pk': self.id,
                                        })
        else:
            return reverse_lazy('shop:cart',
                                kwargs={'pk': self.id,
                                        })


def delete_from_cart(request, pk, good_id):
    if request.method == "GET":
        request.user.cart.goods.remove(Good.objects.get(id=good_id))
        request.user.cart.save()
    return HttpResponseRedirect(reverse('shop:cart', kwargs={'pk': pk}))
