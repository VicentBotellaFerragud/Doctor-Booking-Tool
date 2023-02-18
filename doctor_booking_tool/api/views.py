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


@login_required(login_url='/login')
def api_overview(request):
    return render(request, 'overview.html')


@login_required(login_url='/login')
def api_patients(request):
    users = User.objects.all()

    return render(request, 'patients.html', {'users': users})


@login_required(login_url='/login')
def api_doctors(request):
    doctors = Doctor.objects.all()

    return render(request, 'doctors.html', {'doctors': doctors})


@login_required(login_url='/login')
def api_appointments(request):
    appointments = Appointment.objects.all()

    return render(request, 'appointments.html', {'appointments': appointments})
