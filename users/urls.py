from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm
from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
from .views import signup, dashboard, CustomLoginView
urlpatterns = [
    path("signup/", signup, name="signup"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="home"), name="logout"),
    path("dashboard/", dashboard, name="dashboard"),
]
# Signup View
def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after signup
            return redirect('dashboard')  # Redirect to dashboard
    else:
        form = CustomUserCreationForm()
    return render(request, "users/signup.html", {"form": form})

# Login View
class CustomLoginView(LoginView):
    template_name = "users/login.html"  # Ensure this template exists

# Dashboard View
@login_required
def dashboard(request):
    if request.user.role == "room_seeker":
        return render(request, "users/seeker_dashboard.html")
    elif request.user.role == "room_provider":
        return render(request, "users/provider_dashboard.html")
    return render(request, "users/dashboard.html")  # Default dashboard
