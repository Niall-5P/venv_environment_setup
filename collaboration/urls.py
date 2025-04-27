from django.urls import path
from . import views

app_name = 'collaborate'

urlpatterns = [
    # public submission form
    path('',        views.collaborate,           name='collaborate'),
    path('thanks/', views.thanks,                name='collaborate_thanks'),

    # staff-only CRUD
    path('manage/',          views.CollabListView.as_view(),   name='manage'),
    path('edit/<int:pk>/',   views.CollabUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', views.CollabDeleteView.as_view(), name='delete'),
]
