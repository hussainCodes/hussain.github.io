from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=500)
    auther = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13)
    publisher = models.CharField(max_length=500)
    page = models.IntegerField()
    def __str__(self):
        return self.title

# Create your models here.
