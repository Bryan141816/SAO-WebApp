from django.contrib import admin
from .models import IndividualProfileBasicInfo, TestArray,FileUploadTest, counseling_schedule, studentInfo

class IndividualProfileBasicInfoAdmin(admin.ModelAdmin):
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.get_fields()]
        super().__init__(model, admin_site)

admin.site.register(IndividualProfileBasicInfo)

class StudentInfoAdmin(admin.ModelAdmin):
    list_display = ('studID', 'lrn', 'lastname', 'firstname', 'middlename', 'degree', 'yearlvl', 'sex', 'emailadd', 'contact')
    # Optionally, you can add search_fields, list_filter, etc. to enhance the admin interface
    search_fields = ('lastname', 'firstname', 'lrn', 'degree')
    list_filter = ('degree', 'yearlvl', 'sex')
class counselingSceduleAdmin(admin.ModelAdmin):
    list_display = ('counselingID','dateRecieved','studentID','reason','scheduled_date','scheduled_time','email','status')
    list_editable = ('dateRecieved','reason','scheduled_date','scheduled_time','email','status')


admin.site.register(studentInfo, StudentInfoAdmin)
admin.site.register(counseling_schedule, counselingSceduleAdmin)