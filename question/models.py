from django.db import models

class Question(models.Model):
    TYPE_CHOICES = (
        ('scan', '扫码题'),
        ('single_choice', '单选题'),
        ('multi_choice', '多选题'),
    )

    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=255, choices=TYPE_CHOICES)
    is_active = models.BooleanField(default=True)
    question = models.TextField()
    options = models.TextField(blank=True)
    url = models.URLField(max_length=255, blank=True)
    answer = models.TextField()
    tip = models.TextField(blank=True)
    userAnswer = models.TextField(blank=True, null=True)