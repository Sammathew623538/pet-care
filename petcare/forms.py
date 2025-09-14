from dataclasses import field
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from.models import*
import re


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['username'].required = True

        self.fields['password1'].widget = forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter password'
        })

        self.fields['password2'].widget = forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm password'
        })

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists.")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists.")

        # Allow only letters (no numbers or symbols)
        if not re.match(r'^[A-Za-z_ ]+$', username):
            raise forms.ValidationError("Username should contain only letters.")

        return username

def clean(self):
    cleaned_data = super().clean()
    password1 = cleaned_data.get("password1")
    password2 = cleaned_data.get("password2")

    if password1 and password2 and password1 != password2:
        raise forms.ValidationError("Passwords do not match.")


class ProfileForm(forms.ModelForm):
    class Meta:
        model=profile
        fields="__all__"
        exclude=['user']

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields="__all__"



        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Subject'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'phone_number'}),
            'message': forms.Textarea(attrs={'placeholder': 'Your Message', 'rows': 5}),
        }



SERVICE_CHOICES = [
    ('Bathing', 'Bathing'),
    ('Nail Trimming', 'Nail Trimming'),
    ('Ear Cleaning', 'Ear Cleaning'),
    ('Teeth Brushing', 'Teeth Brushing'),
]


class GroomingForm(forms.ModelForm):
    services = forms.MultipleChoiceField(
        choices=SERVICE_CHOICES,
        widget=forms.CheckboxSelectMultiple,
      
    )

    class Meta:
        model=Grooming
        fields="__all__"
     

SERVICE_CHOICES = [
    ('Obedience Training', 'Obedience Training'),
    ('Behavior Correction', 'Behavior Correction'),
    ('Potty Training', 'Potty Training'),
    ('Trick Training', 'Trick Training'),
]

class tranningForm(forms.ModelForm):
    services = forms.MultipleChoiceField(
        choices=SERVICE_CHOICES,
        widget=forms.CheckboxSelectMultiple,
      
    )

    class Meta:
        model=Tranning
        fields="__all__"



class walkingForm(forms.ModelForm):
    class Meta:
        model = Walking
        fields = '__all__'
        widgets = {
            'time': forms.TimeInput(attrs={
                'type': 'time',          # 🕒 This shows the clock input
               
            }),
        }


class  DoctorForm(forms.ModelForm):
    class Meta :
        model=Doctor
        fields="__all__"





class AppointmentsForm(forms.ModelForm):
    class Meta:
        model = Appointments   # make sure singular class name same as in models.py
        fields = [
            'pet_type',
            'owner_name',
            'Email',
            'reason',
            'date',
            'time',
            'veterinarian',
     
        ] 
        widgets = {
            'time': forms.TimeInput(attrs={
                'type': 'time',          # 🕒 This shows the clock input
               
            }),
        }

        widgets = {
            'date': forms.DateInput(attrs={
                'type': 'date',          # 🕒 This shows the clock input
               
            }),
        }
