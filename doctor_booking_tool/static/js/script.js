const doctorsWrapper = document.getElementById('doctorsWrapper');
const doctorsContainer = document.getElementById('doctorsContainer');
const addNewDoctorForm = document.getElementById('addNewDoctorForm');

function removeDoctorsContainerAndDisplayAddNewDoctorForm() {
    doctorsWrapper.classList.add('d-flex', 'justify-content-center', 'align-items-center');
    doctorsContainer.classList.add('d-none');
    addNewDoctorForm.classList.remove('d-none');
}

const appointmentDatePicker = document.getElementById('appointmentDatePicker');

if (appointmentDatePicker) {
    appointmentDatePicker.min = new Date().toISOString().split('T')[0];
}

const appointmentsWrapper = document.getElementById('appointmentsWrapper');
const appointmentsContainer = document.getElementById('appointmentsContainer');
const addNewAppointmentForm = document.getElementById('addNewAppointmentForm');

function removeAppointmentsContainerAndDisplayAddNewAppointmentForm() {
    appointmentsWrapper.classList.add('d-flex', 'justify-content-center', 'align-items-center');
    appointmentsContainer.classList.add('d-none');
    addNewAppointmentForm.classList.remove('d-none');
}