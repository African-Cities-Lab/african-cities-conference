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
        "000agenda/",
        TemplateView.as_view(template_name="home/agenda.html"),
        name="000agenda",
    ),
]
