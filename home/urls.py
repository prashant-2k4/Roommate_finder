from django.urls import path
from .views import signup, dashboard

urlpatterns = [
    path("signup/", signup, name="signup"),
    path("dashboard/", dashboard, name="dashboard"),
]
