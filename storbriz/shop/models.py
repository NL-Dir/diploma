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
    TYPE_CHOICES = (
        (0, 'Бомберы'),
        (1, 'Ветровки'),
        (2, 'Джинсовые куртки'),
        (3, 'Кожаные куртки'),
        (4, 'Куртки рубашки'),
        (5, 'Пальто'),
        (6, 'Пуховики'),
        (7, 'Тренчи'),
        (8, 'Куртки'),
        (9, 'Водолазки'),
        (10, 'Джемперы'),
        (11, 'Кардиганы'),
        (12, 'Свитеры'),
        (13, 'Джинсы'),
        (14, 'Платья'),
        (15, 'Футболки, поло, лонгсливы'),
        (16, 'Худи, толстовки и свитшоты'),
        (17, 'Брюки'),
        (18, 'Блузы и рубашки'),
        (19, 'Юбки'),
        (20, 'Пиджаки и жакеты'),
        (21, 'Шорты'),
        (22, 'Топы и майки'),
        (23, 'Нижнее белье'),
        (24, 'Спортивная одежда'),
        (25, 'Одежда для дома'),
        (26, 'Обувь'),
        (27, 'Аксессуары'),
    )
    
    name = models.CharField(max_length=255, verbose_name='наименование', null=True, blank=True)
    image_1 = models.ImageField(upload_to='img/', null=True, blank=True, verbose_name='изображение 1')
    image_2 = models.ImageField(upload_to='img/', null=True, blank=True, verbose_name='изображение 2')
    image_3 = models.ImageField(upload_to='img/', null=True, blank=True, verbose_name='изображение 3')
    image_4 = models.ImageField(upload_to='img/', null=True, blank=True, verbose_name='изображение 4')
    is_new = models.BooleanField(default=False, verbose_name='новинка')
    price = models.FloatField(verbose_name='цена', null=True, blank=True)
    type = models.IntegerField(verbose_name='тип', null=True, blank=True, choices=TYPE_CHOICES)
    description = models.TextField(verbose_name='описание', null=True, blank=True)
    color = models.CharField(max_length=20, verbose_name='цвет', null=True, blank=True)
    color_code = models.IntegerField(verbose_name='код цвета', null=True, blank=True)
    article = models.CharField(max_length=20, verbose_name='артикул', null=True, blank=True)


class Cart(models.Model):
    user = models.OneToOneField(User, related_name='cart', on_delete=models.CASCADE)


class Order(models.Model):
    user = models.ForeignKey(User, related_name='order', on_delete=models.CASCADE)
