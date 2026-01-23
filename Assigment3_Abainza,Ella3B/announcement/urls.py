from django.contrib import admin
from django.urls import path, include
from announcements import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('announcements/', include('announcements.urls')),
    path('', views.home, name='home'),  # Home page
]