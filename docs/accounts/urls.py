from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('accounts/', views.index, name='allauth.urls'),
  ]
