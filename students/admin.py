from django.contrib import admin

from students.models import Setting,deparment_info, student_info,staff_info,subject_info

class deparment_infoAdmin(admin.ModelAdmin):
    list_display = ['department_id', 'department_name']
    list_filter = ['department_name']
    list_per_page = 10
    search_fields = ['department_name', 'department_id']
  
admin.site.register(deparment_info,deparment_infoAdmin)
admin.site.register(Setting)

admin.site.register(student_info)
admin.site.register(staff_info)
admin.site.register(subject_info)