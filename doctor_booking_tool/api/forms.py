from django import forms
from .models import Doctor


class NewDoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ('title', 'name', 'gender', 'specialty')

    def save(self):
        super(NewDoctorForm, self).save()
