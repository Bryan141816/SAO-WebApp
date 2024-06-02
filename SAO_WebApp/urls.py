from django.contrib import admin
from django.urls import path
from .views import home, counseling_app,exit_interview,individualProfile,search_student_info,check_date_time_validity,upload_file
from .views import counseling_app_admin_view,ojt_assessment,exit_interview_admin_view, ojt_assessment_admin_view,update_exit_interview_status
from .views import delete_exit_interview_status, update_ojt_assessment, delete_ojt_assessment,check_date_time_validity_for_exit, get_ojt_assessment_data
from .views import search_ojt_assessment_request,search_exit_interview_request, get_exit_interview_request,update_counseling_schedule, delete_counseling_schedule
from .views import search_student_info_for_individual, intake_interview_view, search_student_info_for_intake
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name="Home"),
    #Individual Profile URLS
    path('individual_profile',individualProfile,name="Individual Profile"),
    path('search_student_info_for_individual_profile/', search_student_info_for_individual, name='search_student_info_for_individual_profile'),

    #Intake Interview URLS
    path('intake_interview/',intake_interview_view, name="Intake Interview"),
    path('search_student_info_for_intake/', search_student_info_for_intake, name='search_student_info_for_intake'),

    #Counseling App Views URLS
    path('counseling_app/', counseling_app, name="Counseling App With Scheduler"),
    path('counseling_app/admin/', counseling_app_admin_view, name="Counseling App With Scheduler Admin View"),

    #Counseling App Validator, Updator URLS
    path('check_date_time_validity/',check_date_time_validity,name='check_date_time_validity'),
    path('update_counseling_schedule/', update_counseling_schedule, name='update_counseling_schedule'),
    path('delete_counseling_schedule/', delete_counseling_schedule, name='delete_counseling_schedule'),

    #Exit Interview Views URLS
    path('exit_interview',exit_interview,name="Exit Interview"),
    path('exit_interview/admin/',exit_interview_admin_view,name="Exit Interview Admin View"),
    path('search_exit_interview_request/', search_exit_interview_request, name='search_exit_interview_request'),

    #Exit Interview Searcher, Validator,Updator URLS
    path('search_student_info/', search_student_info, name='search_student_info'),
    path('check_date_time_validity_for_exit/',check_date_time_validity_for_exit,name='check_date_time_validity_for_exit'),
    path('update_exit_interview_status/', update_exit_interview_status, name='update_exit_interview_status'),
    path('delete_exit_interview_status/', delete_exit_interview_status, name='delete_exit_interview_status'),
    path('get_exit_interview_request/',get_exit_interview_request,name="get_exit_interview_request"),

    #OJT Assessment Views URLS
    path('ojt_assessment',ojt_assessment,name="OJT Assessment"),
    path('ojt_assessment/admin/',ojt_assessment_admin_view,name="OJT Assessment Admin View"),
    
    #OJT Assessment Seacher, Validator, Updator URLS
    path('search_ojt_assessment_request/', search_ojt_assessment_request, name='search_ojt_assessment_request'),
    path('update_ojt_assessment/', update_ojt_assessment, name='update_ojt_assessment'),
    path('delete_ojt_assessment/', delete_ojt_assessment, name='delete_ojt_assessment'),
    path('get_ojt_assessment_data/',get_ojt_assessment_data,name="get_ojt_assessment_data"),

    path('upload/', upload_file, name='upload_file'),
]
