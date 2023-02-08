from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name='overview'),
    path('/doctors', views.get_all_doctors, name='doctors')
]