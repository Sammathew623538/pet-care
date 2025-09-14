from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.conf import settings
from django.core.mail import send_mail

from django.shortcuts import get_object_or_404
from .models import Appointments, Pet_Doctor


from .forms import AppointmentsForm

from.models  import *
from.forms import ProfileForm,ContactForm,GroomingForm,tranningForm,walkingForm,DoctorForm


stu = [
    {'name': 'sam', 'course': 'python', 'salary': '10000'},
    {'name': 'sarun', 'course': 'java', 'salary': '10000'},
    {'name': 'Abel', 'course': 'flutter', 'salary': '10000'},
    {'name': 'melbin', 'course': 'devops', 'salary': '10000'}
]


def tech(request):
    return render(request,'home.html',{'stu':stu})

def loginpage(request):
    error_message = None 
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            print("user authenticated")
            return redirect(pets)
        else:
              error_message = "Invalid username or password."
    return render(request, 'login.html',{'error_message': error_message})






def Register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect(loginpage)
          
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})





def profilepage(request):
    usr = request.user
    pro, created = profile.objects.get_or_create(user=usr)
    return render(request, 'profile.html', {'pro': pro})


def proedit(request,):
    pro=profile.objects.get(user=request.user)
    if request.method =="POST":
        form = ProfileForm(request.POST, request.FILES, instance=pro)
        if form.is_valid():
           form.save()
           return redirect(pets)
    else:
        form=ProfileForm(instance=pro)        
    return render(request,'edit_profile.html',{'form':form})



def logoutpage(request):
    logout(request)
    return redirect(loginpage)
    
def pets(request):
    return render(request, 'components/home.html') 



def About(request):
    return render(request,'about.html')



def Contactpage(request):
    submitted = False  
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            submitted = True  # ✅ Success message kaanikan vendi
            form = ContactForm()  # Empty form show cheyyan
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form, 'submitted': submitted})









def groomingss(request):
    return render(request,'grooming.html')


def groomingsss(request):
    return render(request,'grooming.html')



def service(request):
    if request.method == "POST":
        form = GroomingForm(request.POST)
        if form.is_valid():
            form.save()
            data = form.cleaned_data
            return render(request, 'confirm.html', {'data': data})

    else:
        form = GroomingForm()       
    return render(request, 'service.html', {'form': form})


def tranning(request):
    return render(request,'tranning.html')




def Train(request):
    if request.method == "POST":
        form = tranningForm(request.POST)
        if form.is_valid():
            form.save()
            data = form.cleaned_data
            return render(request, 'verify.html', {'data': data})

    else:
        form = tranningForm()       
    return render(request, 'train.html', {'form': form})


def walking(request):
    return render(request,'walking.html')



def gr(request):
    return render(request,'grooming.html')


def tr(request):
    return render(request,'tranning.html')

def ww(request):
    return render(request,'walking.html')



def walkform(request):
    if request.method =="POST":
       form=walkingForm(request.POST)
       if form.is_valid():
        form.save()
        data = form.cleaned_data
        return render(request, 'ok.html', {'data': data})
        
    else:
        form=walkingForm()       
    return render(request,'nadapp.html',{'form':form})



@login_required
def doctor(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctor.html', {'doctors': doctors})


@login_required
def make_appointment(request):
    if request.method == 'POST':
        form = AppointmentsForm(request.POST)
        if form.is_valid():
            appt = form.save(commit=False)
            appt.user = request.user
            appt.Status = 'Pending'
            appt.save()
            send_mail(f'welcome user {appt.user}', f"Hello {appt.user.first_name or appt.user.username},\n\n"
                f"Thank you for booking an appointment with us.\n"
                f"Here are your appointment details:\n\n"
                f"Date: {appt.date}\n"
                f"Time: {appt.time}\n"
                f"Veterinarian: {appt.veterinarian}\n"
                f"Status: {appt.status}\n\n"
                "We will contact you shortly for further updates.\n\n"
                "Best regards,\n"
                "PetCare Team",
                     settings.EMAIL_HOST_USER,[appt.Email])
            return redirect(pets)
    else:
        form = AppointmentsForm()
    return render(request, 'appointment_form.html', {'form': form})


@login_required
def doctor_appointments(request):
    doctor = get_object_or_404(Pet_Doctor, user=request.user)
    appointments_list = Appointments.objects.filter(veterinarian=doctor, status='Pending')
    return render(request, 'doctor_appointments.html', {'appointments': appointments_list})


@login_required
def approve_appointment(request, id):
    user = request.user
     # Staff or superuser can approve any appointment
    if user.is_staff or user.is_superuser:
        appointment = get_object_or_404(Appointments, id=id)
    else:
        # Normal doctor user
        doctor = get_object_or_404(Pet_Doctor, user=user)
        appointment = get_object_or_404(Appointments, id=id, veterinarian=doctor)

    appointment.status = 'Confirmed'
    appointment.save()
    return redirect(pets)

@login_required
def reject_appointment(request, id):
    user = request.user

    if user.is_staff or user.is_superuser:
        appointment = get_object_or_404(Appointments, id=id)
    else:
        doctor = get_object_or_404(Pet_Doctor, user=user)
        appointment = get_object_or_404(Appointments, id=id, veterinarian=doctor)

    appointment.status = 'Rejected'
    appointment.save()
    return redirect(pets)



@login_required
def patient_appointments(request):
    appointments_list = Appointments.objects.filter(user=request.user)
    return render(request, 'patient_appointments.html', {'appointments': appointments_list})
  



@login_required
def admin_dashboard(request):
    if not request.user.is_superuser:
        return HttpResponse("Unauthorized: Only superusers can access this page.", status=403)

    # Core data
    appointments = Appointments.objects.all()
    doctors = Pet_Doctor.objects.all()
    patients = profile.objects.all()

    # Extra data
    contacts = Contact.objects.all()        # from ContactForm
    groomings = Grooming.objects.all()      # from GroomingForm
    trainings =  Tranning.objects.all()      # from tranningForm
    walkings =  Walking.objects.all()        # from walkingForm

    return render(request, 'admin_dashboard.html', {
        'appointments': appointments,
        'doctors': doctors,
        'patients': patients,
        'contacts': contacts,
        'groomings': groomings,
        'trainings': trainings,
        'walkings': walkings,
    })
