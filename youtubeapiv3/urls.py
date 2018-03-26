"""youtubeapiv3 URL Configuration
"""

from django.contrib import admin
from django.urls import path, include

from youtube.views import homepage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='homepage'),
    path('youtube/', include('youtube.urls')),
]
