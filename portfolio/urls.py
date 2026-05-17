from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("project/<int:pk>/", views.project_detail, name="project_detail"),
    path("contact/", views.contact, name="contact"),
    path("contact/success/", views.contact_success, name="contact_success"),
]
