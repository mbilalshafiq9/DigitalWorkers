"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path,include
from Home import views

urlpatterns = [
    path('', views.index, name="index"),
    path('home', views.index, name="index"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('register', views.register, name="register"),
    path('profile', views.profile, name="home_profile"),
    path('find-work', views.find_work, name="find_work"),
    path('post-work', views.post_work, name="post_work"),
    path('find-worker', views.find_worker, name="find_worker"),
    path('search-worker', views.search_worker, name="search_worker"),
    path('search', views.search, name="search"),
    path('about', views.about, name="about"),
    path('dashboard', views.dashboard, name="dashboard"),
    # path('forgot_password', views.forgot_pass, name="forgot_password"),
]
