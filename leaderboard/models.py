from django.db import models

# Create your models here.

class Leaderboard(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    username = models.CharField(max_length=255)
    score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)