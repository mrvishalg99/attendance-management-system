from django.contrib import admin
from .models import *

@admin.register(ATTENDANCE)
class ATTENDANCEModelAdmin(admin.ModelAdmin):
    list_display = ['subject_id', 'attendance_date', 'session_id', 'created_at', 'updated_at']
    
@admin.register(ATTENDANCE_REPORT)
class ATTENDANCE_REPORTModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at']

# admin.site.register(ATTENDANCE)
# admin.site.register(ATTENDANCE_REPORT)
admin.site.register(ATTEND_PIC)