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
    path(
        "marketplace/",
        TemplateView.as_view(template_name="home/static_marketplace.html"),
        name="marketplace",
    ),
    path(
        "marketplace/sauvie/",
        TemplateView.as_view(template_name="home/marketplace/sauvie.html"),
        name="sauvie",
    ),
    path(
        "marketplace/fiwe/",
        TemplateView.as_view(template_name="home/marketplace/fiwe.html"),
        name="fiwe",
    ),
    path(
        "marketplace/rmobility/",
        TemplateView.as_view(template_name="home/marketplace/rmobility.html"),
        name="rmobility",
    ),
    path(
        "marketplace/sniffer-bike/",
        TemplateView.as_view(template_name="home/marketplace/sniffer_bike.html"),
        name="sniffer-bike",
    ),
    path(
        "marketplace/citizon/",
        TemplateView.as_view(template_name="home/marketplace/citizon.html"),
        name="citizon",
    ),
    path(
        "marketplace/229-cadre-de-vie/",
        TemplateView.as_view(template_name="home/marketplace/cadre_de_vie.html"),
        name="229-cadre-de-vie",
    ),
]
