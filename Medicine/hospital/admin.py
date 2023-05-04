from django.contrib import admin
from .models import Doctor, Patient, Reception

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Reception)
