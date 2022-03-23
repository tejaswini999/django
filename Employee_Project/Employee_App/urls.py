from django.contrib import admin
from django.urls import path
from Employee_App import views

urlpatterns = [
    path('', views.index),
]
