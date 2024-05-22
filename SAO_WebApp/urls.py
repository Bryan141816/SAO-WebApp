from django.contrib import admin
from django.urls import path
from .views import home, counseling_app,good_moral,exit_interview,individualProfile,search_student_info,check_date_time_validity,upload_file, counseling_app_admin_view,ojt_assessment,exit_interview_admin_view, ojt_assessment_admin_view,update_exit_interview_status, delete_exit_interview_status
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name="Home"),
    path('counseling_app/', counseling_app, name="Counseling App With Scheduler"),
    path('counseling_app/admin/', counseling_app_admin_view, name="Counseling App With Scheduler Admin View"),
    path('good_moral/',good_moral, name="Good Moral"),
    path('exit_interview',exit_interview,name="Exit Interview"),
    path('exit_interview/admin/',exit_interview_admin_view,name="Exit Interview Admin View"),
    path('ojt_assessment/admin/',ojt_assessment_admin_view,name="OJT Assessment Admin View"),
    path('ojt_assessment',ojt_assessment,name="OJT Assessment"),
    path('individual_profile',individualProfile,name="Individual Profile"),
    path('search_student_info/', search_student_info, name='search_student_info'),
    path('update_exit_interview_status/', update_exit_interview_status, name='update_exit_interview_status'),
    path('delete_exit_interview_status/', delete_exit_interview_status, name='delete_exit_interview_status'),
    path('check_date_time_validity/',check_date_time_validity,name='check_date_time_validity'),
    path('upload/', upload_file, name='upload_file'),
]
