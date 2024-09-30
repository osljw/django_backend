from django.db import models

from user_auth.models import User
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length = 255)
    author = models.CharField(max_length = 255)
    isbn = models.CharField(max_length = 13, unique = False)
    volume = models.CharField(max_length = 10, blank = True, null = True)  # 用于区分上下册等情况
    publication_date = models.DateField(null = True, blank = True)
    publisher = models.CharField(max_length = 255, null = True, blank = True)
    quantity = models.IntegerField(default = 1)
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