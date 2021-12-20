from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .forms import BookForm
from django.http import HttpResponseRedirect


def index(request):
    books = Book.objects.all()
    return render(request, 'index.html', {'books': books})

def addBook(request):

    form = BookForm(request.POST or None)
   # book = Book.objects.all()
    if form.is_valid():
            form.save()
    return render(request, 'addbook.html', {'form': form})

def updateBook(request, id):
    book = Book.objects.get(id=id)
    form = BookForm(request.POST, instance=book)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/books')
    return render(request, 'updatebook.html', {'book': book})

def deleteBook(request, id):
    form = Book.objects.get(id=id)
    form.delete()
    return HttpResponseRedirect('/books')

# Create your views here.
