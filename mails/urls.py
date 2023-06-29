from django.urls import path
from . import views

urlpatterns = [
    path('', views.mails, name='mails'),
    path('add-email/', views.addMail, name='add-email'),
    path('update-email/<str:pk>/', views.updateMail, name='update-email'),
    path('delete-email/<str:pk>/', views.deleteMail, name='delete-email'),

    path('send-email/', views.sendMails, name='send-email'),
]
