from django.urls import path
from . import views


urlpatterns = [
    path('location/<loc>/', views.index, name='index'),
    path('', views.index, name='default_index'),
]
