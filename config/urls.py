from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
# Django administration: uses Django's default admin login
path("admin/", admin.site.urls),

# Custom login page for JADU Notes

# JADU Notes logout
path(
    "accounts/logout/",
    auth_views.LogoutView.as_view(),
    name="logout",
),

# JADU Notes application
path("", include("notes.urls")),


]
