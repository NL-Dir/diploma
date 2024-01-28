# Generated by Django 5.0.1 on 2024-01-28 16:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_good_material_good_recommendation'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartGood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.IntegerField(blank=True, choices=[(0, 'XS'), (1, 'S'), (2, 'M'), (3, 'L'), (4, 'XL'), (5, 'XXL')], null=True, verbose_name='размер')),
                ('cartThrough', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.cart')),
                ('goodThrough', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.good')),
            ],
        ),
    ]
