from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from .models import *

@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')

@login_required
def Hod_home(request):
    return render(request, "hod_home.html")

@login_required
def Teacher_home(request):
    return render(request, "emp_home.html")

@login_required
def Student_home(request):
    return render(request, "Stu_home.html")

def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            user_type = user.user_type
            if user_type == 1:
                return redirect('Hod_home')
            elif user_type == 2:
                return redirect('Teacher_home')
            elif user_type == 3:
                return redirect('Student_home')
            else:
                messages.error(request, "Please Enter Valid Email & Password !..")
                return redirect('login')
        else:
            messages.error(request, "Please Enter Valid Email & Password !..")
            return redirect('login')
    else:
        return render(request, "login.html")
    
@login_required
def add_student(request):
    branch = BRANCH.objects.all()
    session = SESSION.objects.all()
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            registration = request.POST.get('registration')
            father_name = request.POST.get('father_name')
            branch_id = request.POST.get('branch_id')
            blood_group = request.POST.get('blood_group')
            session_id = request.POST.get('session_id')
            semester = request.POST.get('semester')
            mobile = request.POST.get('mobile')
            gender = request.POST.get('gender')
            address = request.POST.get('address')
            profile_pic = request.FILES.get('profile_pic')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            if password1 != password2:
                messages.warning(request, 'Password Do No Match!...')
                return redirect('add_student')
            else:
                if CustomUser.objects.filter(email=email).exists():
                    messages.warning(request,'Email is Already Taken')
                    return redirect('add_student')
                
                if STUDENT.objects.filter(registration_no=registration).exists():
                    messages.warning(request,'Registration is Already Taken')
                    return redirect('add_student')
                
                else:
                    user = CustomUser(
                        name = name,
                        email = email,
                        mobile = mobile,
                        password = password1,
                        user_type = 3
                    )
                    user.set_password(password1)
                    
                    branch = BRANCH.objects.get(id=branch_id)
                    session = SESSION.objects.get(id=session_id)
                    student = STUDENT(
                        admin = user,
                        address = address,
                        branch = branch,
                        session = session,
                        semester = semester,
                        gender = gender,
                        father_name = father_name,
                        blood_group = blood_group,
                        registration_no = registration,
                        profile_pic = profile_pic,
                    )
                    user.save()
                    student.save()
                    messages.success(request, 'Student Data Save Successfully..')
                    return redirect('add_student')
        except:
            messages.error(request, 'Something Went Wrong!!!......')
            return redirect('add_student')
    
    context = {
        'branch': branch,
        'session': session,
    }
    return render(request, 'stu_regs.html', context)

@login_required
def view_student(request):
    student = STUDENT.objects.all()
    context = {
        'student' : student,
    }
    return render(request, 'view_student.html', context)

@login_required
def view_student_teacher(request):
    session = SESSION.objects.all()
    branch = BRANCH.objects.all()
    action = request.GET.get('action')
    student = None
    get_branch = None
    get_session = None
    
    if action is not None:
        if request.method == "POST":
            session_id = request.POST.get('session_id')
            branch_id = request.POST.get('branch_id')
            
            get_session = SESSION.objects.get(id = session_id)
            get_branch = BRANCH.objects.get(id = branch_id)
            
            session = SESSION.objects.filter(id=session_id)
            branch = BRANCH.objects.filter(id=branch_id)
        
            student = STUDENT.objects.filter(session = session_id, branch = branch_id)
        
    context = {
        'session' : session,
        'branch' : branch,
        'student' : student,
        'action': action,
        'get_branch' : get_branch,
        'get_session' : get_session,
    }
    return render(request, 'view_stu_teacher.html', context)

@login_required
def add_teacher(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            department = request.POST.get('department')
            blood_group = request.POST.get('blood_group')
            mobile = request.POST.get('mobile')
            gender = request.POST.get('gender')
            address = request.POST.get('address')
            profile_pic = request.FILES.get('profile_pic')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            if password1 != password2:
                messages.warning(request, 'Password Do No Match!...')
                return redirect('add_teacher')
            else:
                if CustomUser.objects.filter(email=email).exists():
                    messages.warning(request,'Email is Already Taken')
                    return redirect('add_teacher')             
                else:
                    user = CustomUser(
                        name = name,
                        email = email,
                        mobile = mobile,
                        password = password1,
                        user_type = 2
                    )
                    user.set_password(password1)

                    teacher = TEACHER(
                        admin = user,
                        department = department,
                        address = address,
                        gender = gender,
                        blood_group = blood_group,
                        profile_pic = profile_pic,
                    )
                    user.save()
                    teacher.save()
                    messages.success(request, 'Teacher Data Save Successfully..')
                    return redirect('add_teacher')
        except:
            messages.error(request, 'Something Went Wrong!!!......')
            return redirect('add_teacher')
    
    context = {

    }
    return render(request, 'emp_regs.html', context)

@login_required
def add_subject(request):
    branch = BRANCH.objects.all()
    teacher = TEACHER.objects.all()
    
    if request.method == "POST":
        name = request.POST.get('subject')
        branch_id = request.POST.get('branch')
        teacher_id = request.POST.get('teacher')
        
        branch = BRANCH.objects.get(id = branch_id)
        teacher = TEACHER.objects.get(id = teacher_id)
        
        subject = SUBJECT(subject=name, branch=branch, teacher=teacher)
        subject.save()
        messages.success(request, 'Subject added succesfully .....')
        return redirect('add_subject')
    
    context = {
        'branch' : branch,
        'teacher' : teacher,
    }
    
    return render(request, 'add_subject.html', context)

@login_required
def student_details(request):
    return render(request, "stu_details.html")