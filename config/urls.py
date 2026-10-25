from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
# Django administration: uses Django's default admin login
path("admin/", admin.site.urls),

# Custom login page for JADU Notes
path(
    "accounts/login/",
    auth_views.LoginView.as_view(
        template_name="registration/login.html"
    ),
    name="login",
),
# JADU Notes logout
path(
    "accounts/logout/",
    auth_views.LogoutView.as_view(),
    name="logout",
),

# JADU Notes application
path("", include("notes.urls")),


]

