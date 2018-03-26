from django.urls import path
from . import views

app_name = 'youtube'

urlpatterns = [
    path('authorize/', views.authorize_youtube, name='authorize_youtube'),
    path('callback/', views.callback, name='callback_url'),
]
