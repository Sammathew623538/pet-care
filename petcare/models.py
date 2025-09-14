from django.db import models
from django.contrib.auth.models import User

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_images', null=True, blank=True) 

    def __str__(self):
        return str(self.user.username)
    


class Contact(models.Model):
       name=models.CharField()
       email=models.EmailField()
       phone_number=models.IntegerField()
       subject=models.CharField()
       message=models.TextField()
       

PET_TYPE_CHOICES = [
    ('dog', 'Dog'),
    ('cat', 'Cat'),
]


class Grooming(models.Model):
    pet_Type = models.CharField(max_length=100,choices=PET_TYPE_CHOICES)
    owner_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    services = models.CharField(max_length=255)  

PET_TYPE_CHOICES = [
    ('dog', 'Dog'),
    ('cat', 'Cat'),
]


class Tranning(models.Model):
     pet_Type=models.CharField(max_length=100,choices=PET_TYPE_CHOICES)
     owner_name=models.CharField()
     contact_number=models.IntegerField()
     services=models.CharField()
     

pet_choice=[
     ('Dog','Dog'),
     ('Cat','Cat'),
]


Time=[
     ('Morning','Morning'),
     ('Afternoon','Afternoon'),
     ('Evening','Evening'),
]


Durations=[
     ('15 Min','15Min '),
     ('30Min','30Min'),
     ('45Min','45Min'),
     ('1hr','1hr'),
     ('2hr','2hr'),
      
]

class Walking(models.Model):
     pet_type=models.CharField(max_length=100,choices=pet_choice)
     owner_name=models.CharField()
     contact_number=models.IntegerField()
     Address=models.TextField()
     prefered_Time=models.CharField(max_length=100,choices=Time) 
     time=models.TimeField()
     Duration=models.CharField(max_length=100,choices=Durations)           



class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    image = models.ImageField(upload_to='doctors/')  # image support
    def __str__(self):
        return str(self.name)

pet_choice = [
    ('Dog','Dog'),
    ('Cat','Cat'),
]




STATUS_CHOICES = [
    ('Pending', 'Pending'),
    ('Confirmed', 'Confirmed'),
    ('Rejected', 'Rejected'),
]

class Pet_Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    def __str__(self):
        return str(self.user.username)
    
        
    

class Appointments(models.Model):  # class name singular + Capitalized
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pet_type = models.CharField(max_length=100, choices=pet_choice)
    owner_name = models.CharField(max_length=100)
    Email=models.EmailField(null=True)
    reason = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    veterinarian = models.ForeignKey(Pet_Doctor, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
