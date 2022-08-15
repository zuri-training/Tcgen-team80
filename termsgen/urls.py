from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [

    #landing page
    
    path("", views.index, name="home"),

    #products page

    path("products/", views.products, name="products"),

    #sign in and sign up pages

    path("get-started/", views.getstarted, name="getstarted"),
    path("sign-in/", views.signin, name="signin"),
    path("logout/", views.logoutUser, name="logout"),
    path("forgot/", views.forgot, name="forgot"),
    path("user/", views.userPage, name="userpage"),

    #dashboard

    path("dashboard/", views.dashboard, name="dashboard"),
    path("basic-info/", views.basic_info, name="basic_info"),
    path("web-info/", views.web_info, name="web_info"),

    #terms and conditions pages

    path("terms-conditions/", views.terms_and_conditions, name="terms_conditions"),
    path("terms-and-conditions-additional-info/", views.terms_and_conditions_2, name="terms_conditions_2"),
    path("terms-and-conditions-security-info/", views.terms_and_conditions_3, name="terms_conditions_3"),
    path("terms-and-conditions-preview/", views.terms_and_conditions_4, name="terms_conditions_4"),
    path("terms-and-conditions-success/", views.terms_and_conditions_5, name="terms_conditions_5"),
    # path("security-info", views.terms_and_conditions_3, name="terms_conditions_3"),

    #privacy policy pages

    path("privacy/", views.privacy, name="privacy"),
    path("privacy-additional-info/", views.additionalinfo, name="privacy_2"),
    path("privacy-security-info/", views.security, name="privacy_3"),
    path("privacy-preview/", views.previewdoc, name="privacy_4"),

    #return and refund pages

    path("return-refund/", views.return_and_refund, name="return_refund"),
    path("return-refund-refund-and-shipping-information/", views.return_and_refund_2, name="return_refund_2"),
    path("return-refund-additional-information/", views.return_and_refund_3, name="return_refund_3"),
    path("return-refund-4/", views.return_and_refund_4, name="return_refund_4"),
    path("return-refund-5/", views.return_and_refund_5, name="return_refund_5"),

    #disclaimer pages

    #about us and contact us pages
    path("contact-us/", views.contact_us, name="contact_us"),
    path("about-us/", views.about_us, name="about_us"),

]
