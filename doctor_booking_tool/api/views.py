from django.shortcuts import redirect, render
from .models import Doctor, Appointment
from django.contrib.auth.models import User
from .utils import create_four_sample_doctors_if_doctor_table_empty, set_appointments, assign_patient_and_doctor_to_appointment_and_save_it
from .forms import NewDoctorForm, NewAppointmentForm


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

    appointments = set_appointments(request)
    doctors = Doctor.objects.all()
    patients = User.objects.filter(is_superuser=False)

    if request.method == 'POST':
        form = NewAppointmentForm(request.POST)

        if form.is_valid():
            assign_patient_and_doctor_to_appointment_and_save_it(request, form)

            return redirect('/api/appointments')

    form = NewAppointmentForm()

    return render(request, 'appointments.html', {'appointments': appointments, 'doctors': doctors, 'patients': patients})


def appointment_details(request, pk):
    if not request.user.is_authenticated:
        return redirect('/api/overview')

    appointment = Appointment.objects.get(pk=pk)

    if not request.user.is_superuser and appointment.patient != request.user:
        return redirect('/api/appointments')

    if request.method == 'POST':
        appointment.delete()

        return redirect('/api/appointments')

    return render(request, 'appointment-details.html', {'appointment': appointment})
