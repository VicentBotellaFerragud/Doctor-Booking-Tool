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
