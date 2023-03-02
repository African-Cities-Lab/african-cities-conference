from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path(
        "venue-contact/",
        TemplateView.as_view(template_name="home/contact.html"),
        name="contact",
    ),
]
