from django.contrib import admin
from django.urls import path
from .views import home, counseling_app,good_moral,individualProfile,search_student_info,check_date_time_validity,upload_file, counseling_app_admin_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name="Home"),
    path('counseling_app/', counseling_app, name="Counseling App With Scheduler"),
    path('counseling_app_admin/', counseling_app_admin_view, name="Counseling App With Scheduler Admin View"),
    path('good_moral/',good_moral, name="Good Moral"),
    path('individual_profile',individualProfile,name="Individual Profile"),
    path('search_student_info/', search_student_info, name='search_student_info'),
    path('check_date_time_validity/',check_date_time_validity,name='check_date_time_validity'),
    path('upload/', upload_file, name='upload_file'),
]
