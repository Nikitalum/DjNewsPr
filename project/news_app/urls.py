from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('about/', views.about, name='about'),
    path('news/', views.news, name='news'),
    path('details/', views.details)
]