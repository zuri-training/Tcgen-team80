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
    path("privacy-additional-info", views.additionalinfo, name="privacy_2"),
    path("privacy-security-info", views.security, name="privacy_3"),
    path("privacy-preview/", views.previewdoc, name="privacy_4"),
    path("return-refund/", views.return_and_refund, name="return_refund"),
    path("terms-conditions/", views.terms_and_conditions, name="terms_conditions"),

    path("get-started/", views.getstarted, name="getstarted"),
    path("sign-in/", views.signin, name="signin"),
    path("logout/", views.logoutUser, name="logout"),
    path("forgot/", views.forgot, name="forgot"),
    path("user/", views.userPage, name="userpage"),

    path("terms-and-conditions-additional-info/", views.terms_and_conditions_2, name="terms_conditions_2"),
    path("terms-and-conditions-security-info", views.terms_and_conditions_3, name="terms_conditions_3"),
    path("terms-and-conditions-preview/", views.terms_and_conditions_4, name="terms_conditions_4"),
    path("terms-and-conditions-success", views.terms_and_conditions_5, name="terms_conditions_5"),
    # path("security-info", views.terms_and_conditions_3, name="terms_conditions_3"),

]
