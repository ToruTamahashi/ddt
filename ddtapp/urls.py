from django.contrib import admin
from django.urls import path
from .views import hellofunc, GetData

urlpatterns = [
    path('hello/', hellofunc,name='hello'),
    path('list/', GetData.as_view(), name='list')
]