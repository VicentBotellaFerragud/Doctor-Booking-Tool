from .models import Doctor


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


def assign_patient_and_doctor_to_appointment_and_save_it(request, form):
    appointment = form.save(commit=False)
    appointment.patient = request.user
    appointment.doctor = Doctor.objects.get(pk=request.POST.get('doctor'))
    appointment.save()
