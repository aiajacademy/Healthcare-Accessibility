from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)

class Appointment(models.Model):
    doctor = models.ForeignKey(User, related_name='appointments_doctor', on_delete=models.CASCADE)
    patient = models.ForeignKey(User, related_name='appointments_patient', on_delete=models.CASCADE)
    date = models.DateTimeField()
    description = models.TextField()

class HealthRecord(models.Model):
    patient = models.ForeignKey(User, related_name='health_records', on_delete=models.CASCADE)
    data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
