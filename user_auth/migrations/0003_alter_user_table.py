# Generated by Django 3.2.8 on 2022-04-15 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0002_alter_user_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='user',
            table='user_info',
        ),
    ]
