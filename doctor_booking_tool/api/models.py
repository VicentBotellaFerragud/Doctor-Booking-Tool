from django.db import models
import datetime
from django.contrib.auth.models import User


class Doctor(models.Model):
    title_choices = [
        ('Dr.', 'Dr.'),
        ('Prof. Dr.', 'Prof. Dr.'),
        ('Dr. rer. nat.', 'Dr. rer. nat.')
    ]
    gender_choices = [
        ('Masculine', 'Masculine'),
        ('Femenine', 'Femenine')
    ]
    specialty_choices = [
        ('Family medicine', 'Family medicine'),
        ('Pediatrics', 'Pediatrics'),
        ('Urology', 'Urology'),
        ('Dermatology', 'Dermatology'),
        ('Emergency medicine', 'Emergency medicine')
    ]

    title = models.CharField(
        max_length=13, choices=title_choices, default='Dr.')
    name = models.CharField(max_length=30)
    gender = models.CharField(
        max_length=9, choices=gender_choices, default='Masculine')
    specialty = models.CharField(
        max_length=18, choices=specialty_choices, default='Family medicine')

    def __str__(self):
        return self.title + ' ' + self.name


class Appointment(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=120)
    date = models.DateField()
    created_at = models.DateField(default=datetime.date.today)
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
