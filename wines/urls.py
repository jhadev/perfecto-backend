from django.urls import path
from . import views

urlpatterns = [
    path('api/wines/', views.WineListCreate.as_view()),
]