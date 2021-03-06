from django.contrib import admin
from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room>/', views.chat_room, name='room'),
]
