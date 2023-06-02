from django.db import models
from user_auth.models import User
from wangeditor.fields import WangRichTextField

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Travel(models.Model):
    title = models.CharField(max_length=100)
    is_popular = models.BooleanField(default=False, verbose_name='是否热门')
    cover_image = models.ImageField(upload_to='destination_cover/')
    description = WangRichTextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    cities = models.ManyToManyField('City', related_name='travel')
    duration_days = models.IntegerField() # 行程天数
    start_date = models.DateField() # 起始日期
    end_date = models.DateField() # 中止日期
    def __str__(self):
        return self.title

class Person(models.Model):
    name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=18)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS_CHOICES = (
        ('unpaid', '待支付'),
        ('unused', '待使用'),
        ('used', '已使用'),
        ('refund_pending', '待退款'),
        ('refunded', '已退款')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    travel = models.ForeignKey(Travel, on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=1)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_used = models.DateField()
    persons = models.ManyToManyField(Person)
    status = models.CharField(choices=STATUS_CHOICES, default='unpaid', max_length=20)

    def __str__(self):
        return f"{self.quantity} x {self.travel.title} - {self.user.username}"