from django.shortcuts import redirect, render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from .models import Doctor, Appointment
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

# Create your views here.


def redirect_to_api_overview(request):
    return redirect('/api/overview')


def api_overview(request):
    return render(request, 'overview.html')


def api_patients(request):
    if not request.user.is_superuser:
        return redirect('/api/overview')

    patients = User.objects.filter(is_superuser=False)

    return render(request, 'patients.html', {'patients': patients})


def patient_details(request, pk):
    if not request.user.is_superuser:
        return redirect('/api/overview')

    patient = User.objects.get(pk=pk)

    if request.method == 'POST':
        patient.delete()

        return redirect('/api/patients')

    return render(request, 'patient-details.html', {'patient': patient})


def api_doctors(request):
    doctors = Doctor.objects.all()

    return render(request, 'doctors.html', {'doctors': doctors})


def api_appointments(request):
    appointments = Appointment.objects.all()

    return render(request, 'appointments.html', {'appointments': appointments})
