from django.shortcuts import redirect, render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from .models import Doctor, Appointment
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .utils import create_four_sample_doctors_if_doctor_table_empty, assign_patient_and_doctor_to_appointment_and_save_it
from .forms import NewDoctorForm, NewAppointmentForm

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
    if not request.user.is_authenticated:
        return redirect('/api/overview')

    appointments = Appointment.objects.all()
    doctors = Doctor.objects.all()

    if request.method == 'POST':
        form = NewAppointmentForm(request.POST)

        if form.is_valid():
            assign_patient_and_doctor_to_appointment_and_save_it(request, form)

            return redirect('/api/appointments')

    form = NewAppointmentForm()

    return render(request, 'appointments.html', {'appointments': appointments, 'doctors': doctors})


def appointment_details(request, pk):
    if not request.user.is_authenticated:
        return redirect('/api/overview')

    appointment = Appointment.objects.get(pk=pk)

    if request.method == 'POST':
        if appointment.patient == request.user:
            appointment.delete()

            return redirect('/api/appointments')
        else:
            return redirect('/api/appointments')

    return render(request, 'appointment-details.html', {'appointment': appointment})
