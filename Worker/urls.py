# URLS for Worker Dashbaord

from django.urls import path,include
from Worker import views

urlpatterns = [
    path('', views.dashboard, name="worker_dashboard"),
    path('dashboard', views.dashboard, name="worker_dashboard"),
    path('offers', views.offers, name="worker_offers"),
    path('orders', views.orders, name="worker_orders"),
    path('inbox', views.inbox, name="worker_inbox"),
    path('profile', views.profile, name="worker_profile"),
    path('skills', views.skills, name="skills"),
    path('verification', views.verification, name="verification"),
    path('change-password', views.change_password, name="worker_change_password"),
]
