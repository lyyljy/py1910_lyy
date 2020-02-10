"""django06 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
# import App01.views
from App01 import views
from django.urls import path

# 写上app_name
app_name = "App01"

urlpatterns = [
    path('login/', views.login, name='login'),
    path('mark/', views.reply, name='mark'),
    path('home/', views.index, name='home'),
    path('logout/', views.logout, name='logout'),
]
