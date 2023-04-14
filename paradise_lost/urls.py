"""
URL configuration for paradise_lost project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from army_builder.views import get_index, get_dashboard, get_roster_list, get_about
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", get_index, name="index"),
    path("users/dashboard", get_dashboard, name="dashboard"),
    path("accounts/", include("allauth.urls")),
    path("rosters/", get_roster_list, name="roster-list"),
    path("about/", get_about, name="about")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

