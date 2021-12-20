from django.urls import path
from . import views

urlpatterns = [
   path('', views.viewMembers),
   path('addmember/', views.addMember ),
   path('updatemember/<int:id>', views.updateMember)
]