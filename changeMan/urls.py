"""changeMan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path, include
from parts import views
from changes import views as cViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('access/', include('django.contrib.auth.urls')),
    path('dashboard/', cViews.dashboard, name="dashboard"),
    path('parts/spRequest/', views.get_last, name="SPR"),
    path('parts/add/', views.add_part, name="add_part"),
    path('parts/<str:part_number>/', views.part, name="part_summary"),
    path('ecr/<int:ecr_number>/', cViews.ecr_detail, name="ecr_detail"),
    path('ecr/add/', cViews.ecr_add, name="add_ecr"),
    path('ecr/edit/<int:ecr_number>/', cViews.ecr_edit, name="ecr_edit"),
    path('ecr/list/', cViews.ecr_list, name="ecr_list"),
    path('eco/add/', cViews.eco_add, name="add_eco"),
    path('eco/edit/<int:eco_number>/', cViews.eco_edit, name="eco_edit"),
    path('eco/<int:eco_number>/', cViews.eco_detail, name="eco_detail"),
    path('eco/list/', cViews.eco_list, name="eco_list"),
    path('rev/add/<str:drawing_number>/<int:eco_number>/', cViews.revise_drawing, name="add_rev"),
    path('performance/', cViews.performance, name="performance"),
    path('parts/util/add_series/', views.updateSeries, name="update_series"),
    path('parts/', views.part_list, name="part_list"),
]
