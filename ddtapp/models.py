from django.db import models

class TestModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
