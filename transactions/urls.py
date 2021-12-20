from django.urls import path
from . import views

urlpatterns = [
   path('', views.viewTransactions),
   path('addtransaction/', views.addTransactions)
]