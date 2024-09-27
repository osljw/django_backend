from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    status = models.CharField(max_length=10, choices=[
        ('available', '可用'),
        ('borrowed', '已借出'),
        ('lost', '丢失')
    ])

    class Meta: 
        verbose_name = "书籍"