from django.db import models
from django.contrib.auth.models import User

class Appointment(models.Model):
    date = models.DateField(null=True)
    time = models.TimeField(null=True)

    def __str__(self):
        return str(self.date) + ' at ' + str(self.time)
    
class BookedAppointment(models.Model):
    patient = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    appointment = models.ForeignKey(Appointment, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.patient.first_name) + ' ' + str(self.patient.last_name) + ' , ' + str(self.appointment.date) + ' at ' + str(self.appointment.time)

  

    

