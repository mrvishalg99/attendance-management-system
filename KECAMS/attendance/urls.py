from django.urls import path, include
from .import views

urlpatterns = [
    path('Hod/take_attendance/', views.take_attendance, name = 'take_attendance'),
    path('Hod/save_attendance/', views.save_attendance, name = 'save_attendance'),
    path('Hod/view_attendance/', views.view_attendance, name = 'view_attendance'),
    path('Stu_view_attendance/', views.Stu_view_attendance, name = 'Stu_view_attendance'),
    path('all_attend_pic/', views.all_attend_pic, name = 'all_attend_pic'),
]