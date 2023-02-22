from django import forms
from .models import Doctor, Appointment


class NewDoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ('title', 'name', 'gender', 'specialty')

    def save(self):
        super(NewDoctorForm, self).save()


class NewAppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('title', 'description', 'date',)

    def save(self, commit=True):
        appointment = super(NewAppointmentForm, self).save(commit=False)

        if commit:
            appointment.save()

        return appointment
