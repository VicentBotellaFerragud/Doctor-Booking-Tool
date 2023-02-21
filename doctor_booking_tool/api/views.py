from django.shortcuts import redirect, render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from .models import Doctor, Appointment
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .utils import create_four_sample_doctors_if_doctor_table_empty
from .forms import NewDoctorForm

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
    create_four_sample_doctors_if_doctor_table_empty()
    doctors = Doctor.objects.all()

    if request.method == 'POST':
        form = NewDoctorForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/api/doctors')

    form = NewDoctorForm()

    return render(request, 'doctors.html', {'doctors': doctors})


def doctor_details(request, pk):
    doctor = Doctor.objects.get(pk=pk)

    if request.method == 'POST':
        doctor.delete()

        return redirect('/api/doctors')

    return render(request, 'doctor-details.html', {'doctor': doctor})


def api_appointments(request):
    appointments = Appointment.objects.all()

    return render(request, 'appointments.html', {'appointments': appointments})
