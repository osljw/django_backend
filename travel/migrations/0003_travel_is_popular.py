# Generated by Django 3.2.8 on 2023-05-30 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0002_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='travel',
            name='is_popular',
            field=models.BooleanField(default=False, verbose_name='是否热门'),
        ),
    ]