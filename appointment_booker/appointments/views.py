from django.shortcuts import render, redirect
from .models import Appointment, BookedAppointment
from datetime import date
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'appointments/home.html')

@login_required
def booked_appointments(request):    
    patient = request.user
    today = date.today()
    patient_appointments = BookedAppointment.objects.filter(appointment__date__gte=today, patient=patient).order_by('appointment__date')    
    context = {'patient_appointments':patient_appointments}
    return render(request, 'appointments/booked_appointments.html', context)   

@login_required
def available_appointments(request):
    appointments = Appointment.objects.all()  
    booked_appointments = BookedAppointment.objects.all()
    """Retrieve the IDs of already booked appointments"""
    booked_ids = [booked_appointment.appointment.id for booked_appointment in booked_appointments]

    """Filter out booked appointments from list of available appointments"""
    available_appointments = appointments.exclude(id__in=booked_ids)

    """Include only upcoming available appointments in list of available appointments"""
    today = date.today()
    upcoming_appointments = available_appointments.filter(date__gte = today).order_by('date', 'time')
        
    context = {'upcoming_appointments':upcoming_appointments}
    return render(request, 'appointments/available_appointments.html', context)

@login_required
def book_appointment(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    if request.method == 'POST':
        patient = request.user
        add_appointment = BookedAppointment(patient=patient, appointment=appointment)
        add_appointment.save()
        return redirect('booking_confirmation', appointment_id=appointment.id)
    context = {'appointment':appointment}
    return render(request, 'appointments/book_appointment.html', context)

@login_required
def booking_confirmation(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    context = {'appointment':appointment}
    return render(request, 'appointments/booking_confirmation.html', context)

@login_required
def cancel_appointment(request, appointment_id):
    appointment = BookedAppointment.objects.get(id=appointment_id)
    cancelled_appointment = appointment.appointment
    if request.method == 'POST':
        appointment.delete()
        return redirect('cancellation_confirmation', appointment_id=cancelled_appointment.id)
    context = {'appointment':appointment}
    return render(request, 'appointments/cancel_appointment.html', context)

@login_required
def cancellation_confirmation(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    context = {'appointment':appointment}
    return render(request, 'appointments/cancellation_confirmation.html', context)
    
