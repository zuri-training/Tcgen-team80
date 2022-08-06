from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("products/", views.products, name="products"),
    path("contact-us/", views.contact_us, name="contact_us"),
    path("about-us/", views.about_us, name="about_us"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("basic-info/", views.basic_info, name="basic_info"),
    path("web-info/", views.web_info, name="web_info"),
    path("privacy/", views.privacy, name="privacy"),
    path("return-refund/", views.return_and_refund, name="return_refund"),
    path("terms-conditions/", views.terms_and_conditions, name="terms_conditions"),
    path("additional-info/", views.terms_and_conditions_2, name="terms_conditions_2")
]
