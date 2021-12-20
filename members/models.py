from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=255)
    idCard = models.CharField(max_length=6)
    balance = models.FloatField()
    def __str__(self):
        return self.name


# Create your models here.
