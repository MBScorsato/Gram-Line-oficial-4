from django.urls import path
from . import views

urlpatterns = [
    path('index/ranking/', views.ranking, name='ranking'),


]