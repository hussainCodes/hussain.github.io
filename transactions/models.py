from django.db import models
from members.models import Member
from books.models import Book



class Transaction(models.Model):
    borrowedBook = models.CharField(max_length=500)
    memberBorrower = models.CharField(max_length=255)
    fees = models.FloatField()
    destination = models.BooleanField()

