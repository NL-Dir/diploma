from django.contrib.auth.models import User
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
        queryset = {'new_goods': Good.objects.order_by('-is_new', '-id')[:12],
                    'top_goods': Good.objects.filter(is_popular=True)[:12]}
        return queryset


class GoodDetailView(DetailView):
    model = Good
    template_name = 'src/page-product.html'
    context_object_name = 'good'

    def get_success_usl(self):
        if self.request.POST:
            print(self.request.user)
            return reverse_lazy('shop:good',
                                kwargs={'pk': self.id})


class CartDetailView(DetailView):
    model = Cart
    template_name = 'src/basket.html'
    context_object_name = 'cart'


def add_to_cart(request, pk, good_id):
    request.user.cart.goods.add(Good.objects.get(id=good_id))
    request.user.cart.save()
    return HttpResponseRedirect(reverse('shop:good', kwargs={'pk': good_id}))


def delete_from_cart(request, pk, good_id):
    request.user.cart.goods.remove(Good.objects.get(id=good_id))
    request.user.cart.save()
    return HttpResponseRedirect(reverse('shop:cart', kwargs={'pk': pk}))


class UserDetailView(DetailView):
    model = User
    template_name = 'src/personal-account.html'
    context_object_name = 'user'
