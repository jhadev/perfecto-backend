from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/wines/', views.WineListCreate.as_view()),
]