from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.logins,name='login'),
    path('dashboard/',views.dashboard,name='dashboard')
]
