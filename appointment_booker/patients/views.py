from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from patients.forms import RegisterUserForm, EditAccountForm, EditPasswordForm

def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration successful. You can now book an appointment with Dr Ferran."))
            return redirect('home')
        else:
            for error in list(form.errors.values()):
                    messages.error(request, error)
                    return redirect('register')
    else:
        form = RegisterUserForm()
    context = {'form':form}
    return render(request, 'patients/register.html', context)

def patient_login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You are now signed in to your account."))
            return redirect('home')
        else:
            messages.error(request, ("There was a problem signing in. Please check your sign in details and try again."))
            return redirect('patient_login')
    else:    
        return render(request, 'patients/patient_login.html')

def patient_logout(request):
    logout(request)
    messages.success(request, ("You have signed out of your account."))
    return redirect('home')

@login_required
def account(request):
    patient = request.user    
    context = {'patient':patient}
    return render(request, 'patients/account.html', context)

@login_required
def edit_account(request):
    form = EditAccountForm(instance=request.user)
    if request.method == 'POST':
        form = EditAccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been updated.")
            return redirect('account')
        else:
            for error in list(form.errors.values()):
                    messages.error(request, error)
                    return redirect('edit_password')
    context = {'form':form}
    return render(request, 'patients/edit_account.html', context)

@login_required
def edit_password(request):
    if request.user.is_authenticated:
        patient = request.user
        if request.method == 'POST':
            form = EditPasswordForm(patient, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Your password has been updated.")
                login(request, patient)
                return redirect("account")
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
                    return redirect('edit_password')
        else:
            form = EditPasswordForm(patient)
            context = {'form':form}
            return render(request, 'patients/edit_password.html', context)
    else:
        messages.error(request, "Only patients who are signed in can view this page.")
        return redirect('home')

@login_required   
def delete_account(request):
    patient_account = request.user
    if request.method == 'POST':
        patient_account.delete()
        messages.success(request, "Your account has been deleted.")
        return redirect('home')
    return render(request, 'patients/delete_account.html')





