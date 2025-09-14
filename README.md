PetCare Management System

A Django-based web application designed for pet owners 🐶🐱 and veterinary doctors 🩺.
This system helps pet owners book services (✨ grooming, 🎓 training, 🚶 walking) and make appointments with doctors, while doctors and admins can manage schedules 📅 and patient details easily.

🚀 Features
🔑 Authentication & Profile

✅ User registration & login system
✅ Profile creation and editing ✍️
✅ Secure login/logout 🔒

🐕 Pet Owner Features

🐾 Book grooming, training, and walking services
📩 Contact form to reach PetCare team
📅 Make doctor appointments
👀 View own appointments status (⏳ Pending / ✅ Confirmed / ❌ Rejected)

🩺 Doctor Features

📋 View pending appointment requests
👍 Approve / 👎 Reject patient appointments
📅 Manage own schedule

👨‍💻 Admin Features

📊 Dashboard to manage:

📅 Appointments

🩺 Doctors

👥 Patients

📩 Contacts

✨ Groomings / 🎓 Trainings / 🚶 Walkings

📧 Email Notifications

📨 Automatic email confirmation sent to users after booking an appointment

🛠 Tech Stack

🐍 Backend: Django (Python)

🎨 Frontend: HTML, CSS, Django Templates

🗄️ Database: SQLite (default, can switch to PostgreSQL/MySQL)

🔒 Authentication: Django Auth

📧 Email Service: Django send_mail with SMTP

📂 Project Structure
PetCare/
│── petcare/            # ⚙️ Main project settings
│── app/                # 📦 Core app with views, models, forms
│── templates/          # 🎨 HTML templates (login, register, dashboard, etc.)
│── static/             # 🖼️ CSS, JS, Images
│── manage.py           # ▶️ Django project runner

🔧 Setup Instructions

📥 Clone the repo:

git clone https://github.com/Sammathew623538/Doctor-Appointment-Booking-System-.git
cd petcare


🌱 Create and activate virtual environment:

python -m venv venv
source venv/bin/activate   # Linux/Mac 🐧🍏
venv\Scripts\activate      # Windows 🪟


📦 Install dependencies:

pip install -r requirements.txt


🛠 Run migrations:

python manage.py makemigrations
python manage.py migrate


👑 Create superuser (Admin):

python manage.py createsuperuser


▶️ Start server:

python manage.py runserver

📸 Screenshots (Optional)

🔐 Login Page

👤 Profile Page

📊 Admin Dashboard

📅 Appointment Booking

✨ Future Improvements

💳 Online payment integration for services
💬 Live chat with doctor
📜 Pet health records management
📱 Notifications via SMS/WhatsApp

👨‍💻 Author

Developed with ❤️ by [Sam Mathew]
