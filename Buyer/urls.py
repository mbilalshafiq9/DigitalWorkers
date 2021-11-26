# URLS for Buyer Dashbaord

from django.urls import path,include
from Buyer import views

urlpatterns = [
    path('', views.dashboard, name="buyer_dashboard"),
    path('dashboard', views.dashboard, name="buyer_dashboard"),
    path('posted-works', views.posted_works, name="posted_works"),
    path('offers', views.work_offers, name="offers"),
    # path('forgot_password', views.forgot_pass, name="forgot_password"),
]
