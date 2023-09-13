from django.urls import path, include
from .views import WatchListAV, WatchDetailAV, StreamPlateformAV
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('list/',WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/',WatchDetailAV.as_view(), name='movie-detail'),
    
]