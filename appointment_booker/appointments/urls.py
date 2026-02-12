from django.urls import path
from appointments import views as views

urlpatterns = [
    path('', views.home, name='home'),   
    path('booked_appointments', views.booked_appointments, name="booked_appointments"),
    path('available_appointments', views.available_appointments, name="available_appointments"),
    path('book_appointment/<appointment_id>/', views.book_appointment, name="book_appointment"),
    path('booking_confirmation/<appointment_id>/', views.booking_confirmation, name="booking_confirmation"),
    path('cancel_appointment/<appointment_id>/', views.cancel_appointment, name="cancel_appointment"),
    path('cancellation_confirmation/<appointment_id>/', views.cancellation_confirmation, name="cancellation_confirmation"),
]