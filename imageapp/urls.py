from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('addemployee', views.addEmployee, name="addEmployee"),
    path('addimage', views.addImage, name="addImage"),
    path('addexcel', views.addExcel, name="addExcel"),
]
