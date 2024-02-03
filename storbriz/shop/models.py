from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Good(models.Model):
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
    GENDER_CHOICES = (
        (0, 'Мужское'),
        (1, 'Женское'),
        (2, 'Детское'),
    )

    name = models.CharField(max_length=255, verbose_name='наименование', null=True, blank=True)
    image_1 = models.ImageField(upload_to='img/', null=True, blank=True, verbose_name='изображение 1')
    image_2 = models.ImageField(upload_to='img/', null=True, blank=True, verbose_name='изображение 2')
    image_3 = models.ImageField(upload_to='img/', null=True, blank=True, verbose_name='изображение 3')
    image_4 = models.ImageField(upload_to='img/', null=True, blank=True, verbose_name='изображение 4')
    is_new = models.BooleanField(default=False, verbose_name='новинка')
    is_popular = models.BooleanField(default=False, verbose_name='популярный товар')
    price = models.FloatField(verbose_name='цена', null=True, blank=True)
    type = models.IntegerField(verbose_name='тип', null=True, blank=True, choices=TYPE_CHOICES)
    gender = models.IntegerField(verbose_name='пол', null=True, blank=True, choices=GENDER_CHOICES)
    description = models.TextField(verbose_name='описание', null=True, blank=True)
    color = models.CharField(max_length=20, verbose_name='цвет', null=True, blank=True)
    color_code = models.IntegerField(verbose_name='код цвета', null=True, blank=True)
    article = models.CharField(max_length=20, verbose_name='артикул', null=True, blank=True)
    material = models.TextField(verbose_name='состав', null=True, blank=True)
    recommendation = models.TextField(verbose_name='рекомендации', null=True, blank=True)
    goods = models.ManyToManyField('Cart', through='CartGood')


class Cart(models.Model):
    user = models.OneToOneField(User, related_name='cart', on_delete=models.CASCADE)
    goods = models.ManyToManyField(Good, through='CartGood')

    @property
    def goods_cost(self):
        price_sum = 0
        if self.goods:
            for good in self.goods.all():
                price_sum += good.price
        return price_sum

    @property
    def delivery_cost(self):
        cost = 349 if self.goods_cost <= 5000 else 0
        return cost

    @property
    def total(self):
        if self.goods:
            return self.goods_cost + self.delivery_cost
        else:
            return 0


class CartGood(models.Model):
    SIZE_CHOICES = (
        (0, 'XS'),
        (1, 'S'),
        (2, 'M'),
        (3, 'L'),
        (4, 'XL'),
        (5, 'XXL'),

    )
    cartThrough = models.ForeignKey(Cart, on_delete=models.CASCADE)
    goodThrough = models.ForeignKey(Good, on_delete=models.CASCADE)
    size = models.IntegerField(verbose_name='размер', null=True, blank=True, choices=SIZE_CHOICES)


class Order(models.Model):
    TIME_CHOICES = (
        (1, '9:00 - 21:00'),
        (1, '9:00 - 15:00'),
        (1, '15:00 - 21:00'),
        (1, '9:00 - 13:00'),
        (1, '13:00 - 17:00'),
        (1, '17:00 - 21:00'),
    )
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    street = models.CharField(max_length=255, verbose_name='улица', null=True, blank=True)
    building = models.CharField(max_length=15, verbose_name='дом', null=True, blank=True)
    flat = models.CharField(max_length=15, verbose_name='квартира', null=True, blank=True)
    date = models.DateField(verbose_name='дата доставки', null=True, blank=True)
    time_period = models.IntegerField(verbose_name='интервал доставки', null=True, blank=True, choices=TIME_CHOICES)
    total = models.FloatField(verbose_name='сумма', null=True, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(user=instance)
