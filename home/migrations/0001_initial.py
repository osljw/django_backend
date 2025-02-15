# Generated by Django 3.2.8 on 2022-04-10 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_url', models.CharField(max_length=255, verbose_name='img url')),
                ('link_url', models.CharField(max_length=500, verbose_name='link url')),
                ('is_show', models.BooleanField(default=True, verbose_name='should img show')),
                ('orders', models.IntegerField(default=1, verbose_name='img show order')),
                ('title', models.CharField(max_length=500, verbose_name='ad title')),
            ],
            options={
                'verbose_name': 'banner img',
                'db_table': 'banner',
            },
        ),
    ]
