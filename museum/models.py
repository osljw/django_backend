from django.db import models

# Create your models here.


class Museum(models.Model):
    name = models.CharField(max_length=50, unique=True)
    website = models.URLField()
    areaid = models.CharField(max_length=255)

    class Meta:
        db_table = "museum"
        verbose_name = "博物馆"