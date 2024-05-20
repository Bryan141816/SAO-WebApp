from django.contrib import admin
from .models import IndividualProfileBasicInfo, TestArray,FileUploadTest

class IndividualProfileBasicInfoAdmin(admin.ModelAdmin):
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.get_fields()]
        super().__init__(model, admin_site)


admin.site.register(IndividualProfileBasicInfo)