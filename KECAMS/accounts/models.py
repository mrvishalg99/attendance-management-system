from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

class CustomUser(AbstractUser):
    USER = {
        (1, 'HOD'),
        (2, 'TEACHER'),
        (3, 'STUDENT'),
    }
    username = None
    first_name = None
    last_name = None
    email = models.EmailField(('email address'), unique=True)
    name = models.CharField(max_length=150)
    mobile = models.CharField(max_length=10)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    user_type = models.IntegerField(choices = USER, default=1)
    profile_pic = models.ImageField(upload_to='Hod/profile_pic', null=True, blank=True)
    
    objects = UserManager()
    
    def __str__(self):
        return self.email
    
class BRANCH(models.Model):
    branch = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
       
    def __str__(self):
        return self.branch
    
class SESSION(models.Model):
    session = models.CharField(max_length=100)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.session   
    
class STUDENT(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='stu_profile')
    registration_no = models.CharField(max_length=11)
    father_name = models.CharField(max_length=150)
    gender = models.CharField(max_length=100)
    branch = models.ForeignKey(BRANCH, on_delete=models.DO_NOTHING)
    session = models.ForeignKey(SESSION, on_delete=models.DO_NOTHING)
    semester = models.CharField(max_length=50)
    address = models.TextField()
    blood_group = models.CharField(max_length=50)
    profile_pic = models.ImageField(upload_to='Student/profile_pic')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.admin.name
    
class TEACHER(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    department = models.CharField(max_length=180, null=True)
    address = models.TextField()
    gender = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='Teacher/profile_pic')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.admin.name
    
class SUBJECT(models.Model):
    subject = models.CharField(max_length=100)
    branch = models.ForeignKey(BRANCH, on_delete=models.CASCADE)
    teacher = models.ForeignKey(TEACHER, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.subject