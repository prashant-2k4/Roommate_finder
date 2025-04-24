from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm

def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after signup
            messages.success(request, "Signup successful! Redirecting...")
            return redirect("dashboard")  # Redirect to dashboard
    else:
        form = CustomUserCreationForm()

    return render(request, "users/signup.html", {"form": form})

@login_required
def dashboard(request):
    """Redirect user based on their role."""
    
    if getattr(request.user, "role", None) == "room_seeker":
        return render(request, "users/seeker_dashboard.html")
    elif getattr(request.user, "role", None) == "room_provider":
        return render(request, "users/provider_dashboard.html")

    return render(request, "users/dashboard.html")  # Default dashboard

class CustomLoginView(LoginView):
    template_name = "users/login.html"

    def get_success_url(self):
        return "/users/dashboard/"  # Redirect to dashboard after login
