# URLS for Buyer Dashbaord

from django.urls import path,include
from Buyer import views

urlpatterns = [
    path('', views.dashboard, name="buyer_dashboard"),
    path('dashboard', views.dashboard, name="buyer_dashboard"),
    path('posted-works', views.posted_works, name="posted_works"),
    path('offers', views.work_offers, name="offers"),
    path('orders', views.orders, name="orders"),
    path('inbox', views.inbox, name="inbox"),
    path('profile', views.profile, name="profile"),
    path('change-password', views.change_password, name="change_password"),
    # path('forgot_password', views.forgot_pass, name="forgot_password"),
    path('get_review', views.GetReview, name="get_review")
]
