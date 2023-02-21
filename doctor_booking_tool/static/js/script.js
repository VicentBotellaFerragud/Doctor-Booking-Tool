const doctorsWrapper = document.getElementById('doctorsWrapper');
const doctorsContainer = document.getElementById('doctorsContainer');
const addNewDoctorForm = document.getElementById('addNewDoctorForm');

function removeDoctorsContainerAndDisplayAddNewDoctorForm() {
    doctorsWrapper.classList.add('d-flex', 'justify-content-center', 'align-items-center');
    doctorsContainer.classList.add('d-none');
    addNewDoctorForm.classList.remove('d-none');
}