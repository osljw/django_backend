from django.db import models

from user_auth.models import User
# Create your models here.

class Book(models.Model):
    uid = models.CharField(max_length = 13, unique = False, null = True, blank = True)
    isbn = models.CharField(max_length = 13, unique = False, null = True, blank = True)
    title = models.CharField(max_length = 255)
    author = models.CharField(max_length = 255, null = True, blank = True)
    publication_date = models.DateField(null = True, blank = True)
    publisher = models.CharField(max_length = 255, null = True, blank = True)
    total_count = models.IntegerField(default = 1)
    borrowed_count = models.IntegerField(default=0)
    purchase_year = models.IntegerField(null=True, blank=True)
    # status = models.CharField(max_length=10, choices=[
    #     ('available', '可用'),
    #     ('borrowed', '已借出'),
    #     ('lost', '丢失')
    # ])

    class Meta: 
        verbose_name = "书籍"

class Borrow(models.Model):
    book = models.ForeignKey(Book, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    borrow_date = models.DateTimeField(auto_now_add = True)
    return_date = models.DateTimeField(null = True, blank = True)
    # due_date = models.DateTimeField()
    volume = models.CharField(max_length = 10)

    class Meta: 
        verbose_name = "书籍借阅"