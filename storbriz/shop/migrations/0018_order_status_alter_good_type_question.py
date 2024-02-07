# Generated by Django 5.0.1 on 2024-02-07 16:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_remove_order_address_order_street_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(0, 'Создан'), (1, 'Обработан'), (2, 'Собран'), (3, 'Передан в доставку'), (4, 'Получен')], default=0, verbose_name='статус заказа'),
        ),
        migrations.AlterField(
            model_name='good',
            name='type',
            field=models.IntegerField(blank=True, choices=[(0, 'Бомберы'), (1, 'Ветровки'), (2, 'Джинсовые куртки'), (3, 'Кожаные куртки'), (4, 'Куртки рубашки'), (5, 'Пальто'), (6, 'Пуховики'), (7, 'Тренчи'), (8, 'Куртки'), (9, 'Водолазки'), (10, 'Джемперы'), (11, 'Кардиганы'), (12, 'Свитеры'), (13, 'Джинсы'), (14, 'Платья'), (15, 'Футболки'), (16, 'Худи'), (17, 'Брюки'), (18, 'Блузы'), (19, 'Юбки'), (20, 'Пиджаки'), (21, 'Шорты'), (22, 'Топы и майки'), (23, 'Нижнее белье'), (24, 'Спортивная одежда'), (25, 'Одежда для дома'), (26, 'Обувь'), (27, 'Аксессуары'), (28, 'Жакеты'), (29, 'Поло'), (30, 'Лонгсливы'), (31, 'Толстовки'), (32, 'Свитшоты'), (33, 'Рубашки')], null=True, verbose_name='тип'),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Ваш вопрос')),
                ('answer', models.TextField(verbose_name='Ответ службы поддержки')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
