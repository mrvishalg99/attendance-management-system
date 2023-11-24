from django.shortcuts import render, redirect
from accounts.models import *
from .models import *
from .recognition import run_recognition
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def take_attendance(request):
    teacher_id = TEACHER.objects.get(admin=request.user.id)
    subject = SUBJECT.objects.filter(teacher=teacher_id)
    session = SESSION.objects.all()
    action = request.GET.get('action')
    
    get_subject = None
    get_session = None
    students = None
    identified_stu = None
 
    if action == "upload_image":
        if request.method == "POST":
            global images
            images = request.FILES.getlist('images')
            for img in images:
                pic = ATTEND_PIC(attend_pic=img)
                pic.save()
        
    if action == 'get_student':
        if request.method == "POST":
            subject_id = request.POST.get('subject_id')
            session_id = request.POST.get('session_id')
            
            get_subject = SUBJECT.objects.get(id = subject_id)
            get_session = SESSION.objects.get(id = session_id)
            
            subject = SUBJECT.objects.filter(id=subject_id)
            session = SESSION.objects.filter(id=session_id)

            for i in subject:
                student_id = i.branch.id
                students = STUDENT.objects.filter(branch=student_id, session=session_id).order_by('registration_no')
                
            identified_stu = run_recognition(images, get_session)
    
    context = {
        'subject' : subject,
        'session' : session,
        'get_subject' : get_subject,
        'get_session' : get_session,
        'action' : action,
        'students' : students,
        'identified_stu' : identified_stu,
    }
    return render(request, 'attendance.html', context)    

@login_required
def save_attendance(request):
    if request.method == 'POST':
        subject_id = request.POST.get('subject_id')
        session_id = request.POST.get('session_id')
        attendance_date = request.POST.get('date')
        students_id1 = request.POST.getlist('students_id1')
        students_id2 = request.POST.getlist('students_id2')

        get_subject = SUBJECT.objects.get(id = subject_id)
        get_session = SESSION.objects.get(id = session_id)
        
        attendance = ATTENDANCE(subject_id = get_subject, session_id = get_session, attendance_date = attendance_date)
        attendance.save()
        
        for i in students_id1:
            stud_id = int(i)
            p_student = STUDENT.objects.get(id = stud_id)
            
            attendance_report = ATTENDANCE_REPORT(student_id = p_student, attendance_id = attendance)
            attendance_report.save()
            
        for i in students_id2:
            stud_id = int(i)
            p_student = STUDENT.objects.get(id = stud_id)
            
            attendance_report = ATTENDANCE_REPORT(student_id = p_student, attendance_id = attendance)
            attendance_report.save()
        messages.success(request, "Attendance Data Saved Successfully.....")
        return redirect('Teacher_home')
    else:
        messages.error(request, "Something went wrong, Try again.....")
        return redirect('save_attendance')

@login_required
def view_attendance(request):
    teacher_id = TEACHER.objects.get(admin=request.user.id)
    subject = SUBJECT.objects.filter(teacher=teacher_id)
    session = SESSION.objects.all()
    
    action = request.GET.get("action")
    get_subject = None
    get_session = None
    date = None
    Attendance_report = None
    
    if action is not None:
        if request.method == "POST":
            subject_id = request.POST.get('subject_id')
            session_id = request.POST.get('session_id')
            date = request.POST.get('date')
            
            get_subject = SUBJECT.objects.get(id = subject_id)
            get_session = SESSION.objects.get(id = session_id)
            attendance = ATTENDANCE.objects.filter(subject_id = get_subject, session_id = get_session, attendance_date = date)
            for i in attendance:
                attendance_id = i.id
                Attendance_report = ATTENDANCE_REPORT.objects.filter(attendance_id = attendance_id)
    
    context = {
        'subject' : subject,
        'session' : session,
        'action' : action,
        'get_subject' : get_subject,
        'get_session' : get_session,
        'date' : date,
        'Attendance_report' : Attendance_report,
    }
    return render(request, "view_attendance.html", context)

@login_required
def Stu_view_attendance(request):
    student = STUDENT.objects.get(admin = request.user.id)
    subject = SUBJECT.objects.filter(branch = student.branch_id)
    action = request.GET.get("action")
    
    get_subject = None
    att_report = None
    
    if action is not None:
        if request.method == "POST":
            subject_id = request.POST.get('subject_id')
            get_subject = SUBJECT.objects.get(id = subject_id)

            att_report = ATTENDANCE_REPORT.objects.filter(student_id = student, attendance_id__subject_id = subject_id)
            
    context = {
        'subject':subject,
        'action':action,
        'get_subject':get_subject,
        'att_report':att_report,
    }
    return render(request, "Stu_view_attendance.html", context)

def all_attend_pic(request):
    pic = ATTEND_PIC.objects.all()
    
    context = {
        'pic' : pic,
    }
    return render(request, "all_attend_pic.html", context)