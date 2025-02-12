"""
URL configuration for personalWebsiteProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from personalWebsiteApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page),
    path('about-me/', views.about_me_page),
    path('about-website/', views.about_website_page),
    path('projects/', views.projects_page),
    path('cv/', views.cv_page),
    path('ziad/', views.ziad_page),
]
