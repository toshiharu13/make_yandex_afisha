from django.urls import path
from places import views

urlpatterns = [
    path('', views.index, name='index')
]
