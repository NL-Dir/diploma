from django.contrib.auth.models import User
from django.db import models


class Person(models.Model):
    user = models.OneToOneField(User, related_name='person', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, verbose_name='телефон', null=True, blank=True)


class Good(models.Model):
    # SIZE_CHOICES = (
    #     (0, 'XS'),
    #     (1, 'S'),
    #     (2, 'M'),
    #     (3, 'L'),
    #     (4, 'XL'),
    #     (5, 'XXL'),
    #
    # )
    name = models.CharField(max_length=255, verbose_name='наименование', null=True, blank=True)
    image_1 = models.ImageField(upload_to='img/', null=True, blank=True, verbose_name='изображение 1')
    image_2 = models.ImageField(upload_to='img/', null=True, blank=True, verbose_name='изображение 2')
    image_3 = models.ImageField(upload_to='img/', null=True, blank=True, verbose_name='изображение 3')
    image_4 = models.ImageField(upload_to='img/', null=True, blank=True, verbose_name='изображение 4')
    is_new = models.BooleanField(default=False, verbose_name='новинка')
    price = models.FloatField(verbose_name='цена', null=True, blank=True)
    description = models.TextField(verbose_name='описание', null=True, blank=True)
    color = models.CharField(max_length=20, verbose_name='цвет', null=True, blank=True)
    color_code = models.IntegerField(verbose_name='код цвета', null=True, blank=True)
    article = models.CharField(max_length=20, verbose_name='артикул', null=True, blank=True)


class Cart(models.Model):
    user = models.OneToOneField(User, related_name='cart', on_delete=models.CASCADE)


class Order(models.Model):
    user = models.ForeignKey(User, related_name='order', on_delete=models.CASCADE)
