from django.urls import path
from room.views import rooms,room

urlpatterns = [
    path('',rooms,name='rooms'),
    path('<slug:slug>/',room,name='room'),
]
