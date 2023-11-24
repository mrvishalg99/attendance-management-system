from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

@admin.register(STUDENT)
class STUDENTModelAdmin(admin.ModelAdmin):
    list_display = ['registration_no','father_name','branch_id','session_id',
    'blood_group','gender','address', 'created_at', 'updated_at']
    
@admin.register(SESSION)
class SessionModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'session']
    
@admin.register(BRANCH)
class BranchModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'branch', 'created_at']
    
# @admin.register(TEACHER)
# class TEACHERModelAdmin(admin.ModelAdmin):
#     list_display = ['name', 'email', 'mobile',
#     'blood_group','gender','address','profile_pic', 'created_at', 'updated_at']

admin.site.register(CustomUser)
admin.site.register(TEACHER)
admin.site.register(SUBJECT)
# admin.site.register(STUDENT)