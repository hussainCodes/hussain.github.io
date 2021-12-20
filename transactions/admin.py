from django.contrib import admin
from .models import Transaction


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('borrowedBook', 'memberBorrower', 'fees', 'destination')


admin.site.register(Transaction, TransactionAdmin)
