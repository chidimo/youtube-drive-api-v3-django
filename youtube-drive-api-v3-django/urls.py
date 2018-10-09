"""youtube-drive-api-v3-django URL Configuration
"""

from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('google-api/', include('google_api.urls')),
]
