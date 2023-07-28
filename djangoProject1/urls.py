"""djangoProject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path('student/', include("student.urls")),
    path("new_stu/", views.new_stu, name="new_stu"),
    path("add_stu/", views.add_stu, name="add_stu"),
    path("stu_info/", views.stu_info, name="stu_info"),
    path("back/", views.back, name="back"),
    path("update_info/", views.update_info, name="update_info"),
    path("check_stu/", views.check_stu, name = "check_stu"),
    path("submit/", views.submit, name = "submit"),
    path("fee_update/", views.fee_update, name="fee_update"),
    path("fee_detail/", views.fee_detail, name="fee_detail"),
    path("fees1/<int:id>/", views.fees1, name="fees1"),
    path("fee_info/", views.fee_info, name="fee_info"),
    path("stu_fees/", views.stu_fees, name="stu_fees"),
    path("scho_info/", views.scho_info, name="scho_info"),
    path("info/<int:id>/", views.info, name="info"),
]
