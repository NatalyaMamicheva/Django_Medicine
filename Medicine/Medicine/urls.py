from django.contrib import admin
from django.urls import path
from hospital.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('doctors/', DoctorList.as_view(), name='doctors_list'),
    path('doctor/detail/<int:pk>/', DoctorDetail.as_view(),
         name='doctor_detail'),
    path('doctor/create/', DoctorCreate.as_view(), name='doctor_create'),
    path('doctor/update/<int:pk>/', DoctorUpdate.as_view(),
         name='doctor_update'),
    path('doctor/delete/<int:pk>/', DoctorDelete.as_view(),
         name='doctor_delete'),
    path('patients/', PatientList.as_view(), name='patients_list'),
    path('patient/detail/<int:pk>/', PatientDetail.as_view(),
         name='patient_detail'),
    path('patient/create/', PatientCreate.as_view(), name='patient_create'),
    path('patient/update/<int:pk>/', PatientUpdate.as_view(),
         name='patient_update'),
    path('patient/delete/<int:pk>/', PatientDelete.as_view(),
         name='patient_delete'),
    path('receptions/', ReceptionsList.as_view(), name='receptions_list'),
    path('reception/detail/<int:pk>/', ReceptionDetail.as_view(),
         name='reception_detail'),
    path('reception/create/', ReceptionCreate.as_view(),
         name='reception_create'),
    path('reception/update/<int:pk>/', ReceptionUpdate.as_view(),
         name='reception_update'),
    path('reception/delete/<int:pk>/', ReceptionDelete.as_view(),
         name='reception_delete')
]
