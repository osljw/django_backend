# Generated by Django 3.2.8 on 2024-11-22 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_management', '0002_auto_20240930_1719'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='quantity',
            new_name='total_count',
        ),
        migrations.RemoveField(
            model_name='book',
            name='volume',
        ),
        migrations.AddField(
            model_name='book',
            name='borrowed_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='book',
            name='purchase_year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='uid',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
    ]