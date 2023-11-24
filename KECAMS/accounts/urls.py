from django.urls import path, include
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', views.login, name = 'login'),
    path('Hod/Home/', views.Hod_home, name = 'Hod_home'),
    path('Teacher/Home/', views.Teacher_home, name = 'Teacher_home'),
    path('Student/Home/', views.Student_home, name = 'Student_home'),
    path('logout/', views.logout, name = 'logout'),
    path('Hod/add_student/', views.add_student, name = 'add_student'),
    path('Hod/add_teacher/', views.add_teacher, name = 'add_teacher'),
    path('Hod/view_student/', views.view_student, name = 'view_student'),
    path('Teacher/view_student/', views.view_student_teacher, name = 'view_student_teacher'),
    path('Hod/student_details/', views.student_details, name = 'student_details'),
    path('Hod/add_subject/', views.add_subject, name = 'add_subject'),
    path('accounts/', include('attendance.urls'), name='attendance'),    
]
