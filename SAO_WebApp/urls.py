from django.contrib import admin
from django.urls import path
from .views import home, counseling_app
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name="Home"),
    path('counseling_app/', counseling_app, name="Counseling App With Scheduler")
]
