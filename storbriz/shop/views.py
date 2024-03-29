from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.forms import modelformset_factory
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import UserCreationForm

from .forms import UserRegisterForm, UserUpdateForm, OrderCreateForm, QuestionCreateForm
from .models import Good, Cart


class GoodsList(ListView):
    model = Good
    template_name = 'src/home.html'
    context_object_name = 'goods'

    def get_queryset(self):
        queryset = {'new_female': Good.objects.filter(gender=1).order_by('-is_new', '-id')[:12],
                    'top_female': Good.objects.filter(is_popular=True, gender=1)[:12],
                    'new_male': Good.objects.filter(gender='0').order_by('-is_new', '-id')[:12],
                    'top_male': Good.objects.filter(is_popular=True, gender='0')[:12],
                    'new_children': Good.objects.filter(gender='2').order_by('-is_new', '-id')[:12],
                    'top_children': Good.objects.filter(is_popular=True, gender='2')[:12],
                    }
        return queryset


class GoodsFilteredList(ListView):
    model = Good
    template_name = 'src/category.html'
    context_object_name = 'goods'

    def get_queryset(self, **kwargs):
        queryset = {
            'new_female': Good.objects.filter(gender=1, type=self.kwargs.get('pk')).order_by('-is_new', '-id')[:12],
            'top_female': Good.objects.filter(is_popular=True, gender=1, type=self.kwargs.get('pk'))[:12],
            'new_male': Good.objects.filter(gender='0', type=self.kwargs.get('pk')).order_by('-is_new', '-id')[:12],
            'top_male': Good.objects.filter(is_popular=True, gender='0', type=self.kwargs.get('pk'))[:12],
            'new_children': Good.objects.filter(gender='2', type=self.kwargs.get('pk')).order_by('-is_new', '-id')[:12],
            'top_children': Good.objects.filter(is_popular=True, gender='2', type=self.kwargs.get('pk'))[:12],
        }
        return queryset


class GoodsSearchList(ListView):
    model = Good
    template_name = 'src/search.html'
    context_object_name = 'goods'

    def get_queryset(self):
        queryset = Good.objects.filter(name__icontains=self.request.GET['word']).order_by('-is_new', '-id')[:12]
        return queryset


class GoodDetailView(DetailView):
    model = Good
    template_name = 'src/page-product.html'
    context_object_name = 'good'

    def get_success_usl(self):
        if self.request.POST:
            return reverse_lazy('shop:good',
                                kwargs={'pk': self.id})


class CartDetailView(DetailView):
    model = Cart
    template_name = 'src/basket.html'
    context_object_name = 'cart'


def add_to_cart(request, pk, good_id):
    print(request)
    request.user.cart.goods.add(Good.objects.get(id=good_id), through_defaults={"size": request.GET['size']})
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


class UserCreateView(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    template_name = 'registration/registration.html'


class UserUpdateView(UpdateView):
    form_class = UserUpdateForm
    template_name = 'registration/registration.html'

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('account', kwargs={'pk': self.object.id})


class OrderCreateView(CreateView):
    form_class = OrderCreateForm
    template_name = 'src/page-delivery.html'

    def get_success_url(self):
        return reverse_lazy('account', kwargs={'pk': self.object.user.id})

    def get_initial(self, *args, **kwargs):
        initial = super(OrderCreateView, self).get_initial(**kwargs)
        initial['user'] = self.request.user
        initial['total'] = self.request.user.cart.total
        initial['goods'] = self.request.user.cart.goods.all()
        return initial


class QuestionCreateView(SuccessMessageMixin, CreateView):
    form_class = QuestionCreateForm
    template_name = 'src/support-service.html'
    success_message = 'Спасибо за Ваше обращение, мы свяжемся с Вами в ближайшее время'

    def get_success_url(self):
        return self.request.path

    def get_initial(self, *args, **kwargs):
        initial = super(QuestionCreateView, self).get_initial(**kwargs)
        initial['user'] = self.request.user
        return initial
