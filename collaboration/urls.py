# collaboration/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('',          views.collaborate, name='collaborate'),
    path('thanks/',   views.thanks,      name='collaborate_thanks'),
]
