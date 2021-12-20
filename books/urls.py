from django.urls import path
from . import views

urlpatterns = [
   path('', views.index),
   path('addbook/', views.addBook),
   path('updatebook/<int:id>', views.updateBook)
]

