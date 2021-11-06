from django.urls import path, include

from . import views

app_name = "dashboard"
urlpatterns = [
    path(
        "dashboard/",
        views.DashboardView.as_view(template_name="dashboard/landing.html"),
        name="landing",
    ),
]
