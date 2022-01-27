from django.urls import path

from places import views

urlpatterns = [
    path('<int:place_id>/', views.places, name='place')
]
