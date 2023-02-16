from django.urls import path, include
from .views import DoctorViewSet, AppointmentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'doctors', DoctorViewSet, basename='doctors')
router.register(r'appointments', AppointmentViewSet, basename='appointments')

urlpatterns = [
    path('', include(router.urls))
]
