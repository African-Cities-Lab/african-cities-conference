from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path(
        "venue-contact/",
        TemplateView.as_view(template_name="home/contact.html"),
        name="contact",
    ),
    path("newsletter/", views.newsletter_submission, name="newsletter"),
    path(
        "program-pdf/",
        TemplateView.as_view(template_name="home/program_pdf.html"),
        name="program-pdf",
    ),
    path(
        "program/",
        TemplateView.as_view(template_name="home/agenda.html"),
        name="program",
    ),
]
