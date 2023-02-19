from django.urls import path
from . import views

urlpatterns = [
    path('', views.redirect_to_api_overview),
    path('overview', views.api_overview, name='overview'),
    path('patients', views.api_patients, name='patients'),
    path('patients/<int:pk>', views.patient_details, name='patient-details'),
    path('doctors', views.api_doctors, name='doctors'),
    path('appointments', views.api_appointments, name='appointments')
]
