# URLS for Worker Dashbaord

from django.urls import path,include
from Worker import views

urlpatterns = [
    path('', views.dashboard, name="worker_dashboard"),
    path('dashboard', views.dashboard, name="worker_dashboard"),
    # path('forgot_password', views.forgot_pass, name="forgot_password"),
]
