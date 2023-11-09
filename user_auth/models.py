from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, ImageField 
# Create your models here.


class User(AbstractUser):
    phone = CharField(max_length=15, verbose_name="电话号码")
    avatar = ImageField(upload_to='user/avatar', blank=True, verbose_name="头像")


    class Meta:
        db_table = "user_info"
        verbose_name = "用户信息"

    def __str__(self) -> str:
        return self.username