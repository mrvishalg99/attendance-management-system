from django.db import models
from accounts.models import *

class ATTEND_PIC(models.Model):
    attend_pic = models.FileField(upload_to='attend_pic', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
class ATTENDANCE(models.Model):
    subject_id = models.ForeignKey(SUBJECT, on_delete=models.DO_NOTHING)
    attendance_date = models.DateField()
    session_id = models.ForeignKey(SESSION, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.subject_id.subject

class ATTENDANCE_REPORT(models.Model):
    student_id = models.ForeignKey(STUDENT, on_delete=models.DO_NOTHING)
    attendance_id = models.ForeignKey(ATTENDANCE, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.student_id.admin.name
    