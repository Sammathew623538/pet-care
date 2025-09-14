from django.urls import path
from petcare.views import *




urlpatterns = [
    path('home',tech),
    path('login',loginpage,name='Loo'),
    path('register', Register, name='register'),
    path('profile',profilepage,name='profile'),
    path('profileedit',proedit,name='edit_profile'),
    path('out',logoutpage,name='ooo'),
    path('house',pets,name='hm'),
    path('aby',About,name='about'),
    path('contact',Contactpage,name='cont'),
    path('grooming',groomingss,name='groomings'),
    path('groomings',groomingsss,name='groom'),
    path('service',service,name='services'),
    path('train',tranning,name='trainn'),
    path('walk',walking,name='walkin'),
    path('trr',Train,name='book'),
    path('ggg',gr,name='gg'),
   path('p',tr,name='tr'),
   path('w',ww,name='wal'),
   path('naa',walkform,name='nadakk'),
   path('doc',doctor,name='doct'),
   path('appointment',make_appointment,name='appoint'),
   path('appointment',make_appointment,name='care'),
   path('accept/<int:id>/', approve_appointment, name='approve_appointment'),
   path('reject/<int:id>/', reject_appointment,name='reject_appointment'),
   path('patient',patient_appointments,name='status'),
   path('docs',doctor_appointments,name='appoos'),
   path('admin',admin_dashboard,name='dash')





   

]

