from django.urls import path
from patients import views as views
from django.contrib.auth import views as auth_views

urlpatterns = [    
    path('account', views.account, name="account"),
    path('register', views.register, name="register"),    
    path('patient_login', views.patient_login, name="patient_login"),    
    path('patient_logout', views.patient_logout, name="patient_logout"),    
    path('edit_account', views.edit_account, name="edit_account"),
    path('edit_password', views.edit_password, name="edit_password"),
    path('delete_account', views.delete_account, name="delete_account"),
    path('password-reset', auth_views.PasswordResetView.as_view(template_name='patients/password_reset.html'), name='password_reset'),
    path('password-reset/done', auth_views.PasswordResetDoneView.as_view(template_name='patients/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='patients/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done', auth_views.PasswordResetCompleteView.as_view(template_name='patients/password_reset_complete.html'), name='password_reset_complete'),
]