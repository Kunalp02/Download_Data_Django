from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.cheatsheet, name="cheatsheet"),
    path('download/<int:cheatsheet_id>/', views.download_cheatsheet, name='download_cheatsheet'),
]
