# Generated by Django 3.2.8 on 2024-11-27 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_management', '0004_book_gift_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='borrow',
            name='volume',
        ),
    ]
