from django.contrib import admin
from django.urls import path
from .views import home, counseling_app,good_moral,individualProfile,test
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name="Home"),
    path('counseling_app/', counseling_app, name="Counseling App With Scheduler"),
    path('good_moral/',good_moral, name="Good Moral"),
    path('individual_profile',individualProfile,name="Individual Profile"),
    path('test',test,name="Test")
]
