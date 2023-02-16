from rest_framework.reverse import reverse
from django.shortcuts import redirect, render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from .serializers import DoctorSerializer, AppointmentSerializer
from .models import Doctor, Appointment
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all().order_by('id')
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request):
        data = {
            'title': request.data.get('title'),
            'name': request.data.get('name'),
            'specialty': request.data.get('specialty')
        }

        serializer = DoctorSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            queryset = Doctor.objects.all().order_by('id')
            serializer = DoctorSerializer(queryset, many=True)

            return Response(serializer.data)

        else:
            return Response(serializer.errors)

    def update(self, request, *args, **kwargs):
        data = {
            'title': request.data.get('title'),
            'name': request.data.get('name'),
            'specialty': request.data.get('specialty')
        }

        doctor_to_edit = self.get_object()
        serializer = DoctorSerializer(instance=doctor_to_edit, data=data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        else:
            return Response(serializer.errors)

    def destroy(self, request, *args, **kwargs):
        doctor_to_delete = self.get_object()
        doctor_to_delete.delete()

        return Response('Doctor deleted')


class AppointmentViewSet(viewsets.ModelViewSet):
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Appointment.objects.filter(patient=self.request.user).order_by('id')

    def create(self, request):
        data = {
            'title': request.data.get('title'),
            'description': request.data.get('description'),
            'date': request.data.get('date'),
            'created_at': request.data.get('created_at'),
            'patient': request.data.get('patient'),
            'doctor': request.data.get('doctor')
        }

        if request.data.get('patient') != self.request.user:
            return Response('You are not allowed to create or modify an appointment for a patient other than yourself.')

        serializer = AppointmentSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            queryset = Appointment.objects.filter(
                patient=self.request.user).order_by('id')
            serializer = AppointmentSerializer(queryset, many=True)

            return Response(serializer.data)

        else:
            return Response(serializer.errors)

    def update(self, request, *args, **kwargs):
        data = {
            'title': request.data.get('title'),
            'description': request.data.get('description'),
            'date': request.data.get('date'),
            'created_at': request.data.get('created_at'),
            'patient': request.data.get('patient'),
            'doctor': request.data.get('doctor')
        }

        appointment_to_edit = self.get_object()
        serializer = AppointmentSerializer(
            instance=appointment_to_edit, data=data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        else:
            return Response(serializer.errors)

    def destroy(self, request, *args, **kwargs):
        appointment_to_delete = self.get_object()
        appointment_to_delete.delete()

        return Response('Appointment deleted')
