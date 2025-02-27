from django.urls import path
from . import views

urlpatterns = [
    path('form', views.car_form, name='car_form'),
]
