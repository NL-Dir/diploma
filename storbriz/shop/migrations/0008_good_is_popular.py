# Generated by Django 5.0.1 on 2024-01-27 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_alter_good_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='is_popular',
            field=models.BooleanField(default=False, verbose_name='популярный товар'),
        ),
    ]
