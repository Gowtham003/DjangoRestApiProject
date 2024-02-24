from django.urls import path
from api import views

urlpatterns = [
    path('', views.api_home), #localhost:8000/api/
    path('echo/', views.echo_echo), #localhost:8000/api/echo
]
