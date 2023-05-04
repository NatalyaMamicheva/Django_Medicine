from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, \
    UpdateView, DeleteView

from hospital.models import Doctor, Patient, Reception


class DoctorList(ListView):
    model = Doctor
    template_name = 'hospital/doctors/list_doctors.html'


class DoctorDetail(DetailView):
    model = Doctor
    template_name = 'hospital/doctors/detail_doctor.html'


class DoctorCreate(CreateView):
    model = Doctor
    template_name = 'hospital/doctors/create_doctor.html'
    fields = ['first_last_middle_name', 'age', 'position']
    success_url = reverse_lazy('doctors_list')


class DoctorUpdate(UpdateView):
    model = Doctor
    template_name = 'hospital/doctors/update_doctor.html'
    fields = ['first_last_middle_name', 'age', 'position']
    success_url = reverse_lazy('doctors_list')


class DoctorDelete(DeleteView):
    model = Doctor
    template_name = 'hospital/doctors/delete_doctor.html'
    success_url = reverse_lazy('doctors_list')


class PatientList(ListView):
    model = Patient
    template_name = 'hospital/patients/list_patients.html'


class PatientDetail(DetailView):
    model = Patient
    template_name = 'hospital/patients/detail_patient.html'


class PatientCreate(CreateView):
    model = Patient
    template_name = 'hospital/patients/create_patient.html'
    fields = ['first_last_middle_name', 'age', 'address', 'gender']
    success_url = reverse_lazy('patients_list')


class PatientUpdate(UpdateView):
    model = Patient
    template_name = 'hospital/patients/update_patient.html'
    fields = ['first_last_middle_name', 'age', 'address', 'gender']
    success_url = reverse_lazy('patients_list')


class PatientDelete(DeleteView):
    model = Patient
    template_name = 'hospital/patients/delete_patient.html'
    success_url = reverse_lazy('patients_list')


class ReceptionsList(ListView):
    model = Reception
    template_name = 'hospital/receptions/list_receptions.html'


class ReceptionDetail(DetailView):
    model = Reception
    template_name = 'hospital/receptions/detail_reception.html'


class ReceptionCreate(CreateView):
    model = Reception
    template_name = 'hospital/receptions/create_reception.html'
    fields = ['date', 'disease', 'cost', 'doctor_name', 'patient_name']
    success_url = reverse_lazy('receptions_list')


class ReceptionUpdate(UpdateView):
    model = Reception
    template_name = 'hospital/receptions/update_reception.html'
    fields = ['date', 'disease', 'cost', 'doctor_name', 'patient_name']
    success_url = reverse_lazy('receptions_list')


class ReceptionDelete(DeleteView):
    model = Reception
    template_name = 'hospital/receptions/delete_reception.html'
    success_url = reverse_lazy('receptions_list')
