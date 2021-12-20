from django.contrib import admin
from .models import Book



class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'auther', 'isbn', 'publisher', 'page')


admin.site.register(Book, BookAdmin)


# Register your models here.
