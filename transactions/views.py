from django.shortcuts import render
from .models import Transaction
from .models import Member
from .models import Book

def viewTransactions(request):
    transactions = Transaction.objects.all()
    return render(request, 'viewTransactions.html', {'transactions': transactions})

def addTransactions(request):
    members = Member.name
    books = Book.title
    transaction = Transaction(request.POST)
    return render(request, 'addTransaction.html', {'members': members, 'books': books})


