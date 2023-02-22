from .models import Doctor, Appointment
from django.contrib.auth.models import User


def create_four_sample_doctors_if_doctor_table_empty():
    if Doctor.objects.all().count() == 0:
        Doctor.objects.bulk_create([
            Doctor(title='Dr.', name='Sarah Jones', gender='Femenine',
                   specialty='Family medicine'),
            Doctor(title='Dr.', name='Daniel Brown',
                   gender='Masculine', specialty='Pediatrics'),
            Doctor(title='Prof. Dr.', name='Alfred Cole',
                   gender='Masculine', specialty='Urology'),
            Doctor(title='Prof. Dr.', name='Elizabeth Miller',
                   gender='Femenine', specialty='Dermatology')
        ])


def set_appointments(request):
    if request.user.is_superuser:
        return Appointment.objects.all()
    else:
        return Appointment.objects.filter(patient=request.user)


def assign_patient_and_doctor_to_appointment_and_save_it(request, form):
    appointment = form.save(commit=False)
    appointment.patient = set_patient(request)
    appointment.doctor = Doctor.objects.get(pk=request.POST.get('doctor'))
    appointment.save()


def set_patient(request):
    if request.user.is_superuser:
        return User.objects.get(pk=request.POST.get('patient'))
    else:
        return request.user
