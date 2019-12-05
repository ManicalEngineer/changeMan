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
from projects import views as pViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('access/', include('django.contrib.auth.urls')),
    path('', cViews.dashboard, name="dashboard"),
    path('parts/spRequest/', views.get_last, name="SPR"),
    path('parts/add/', views.add_part, name="add_part"),
    path('part/', views.part, name="part_summary"),
    path('parts/util/add_series/', views.updateSeries, name="update_series"),
    path('parts/', views.part_list, name="part_list"),
    path('parts/edit/<str:part_number>/', views.edit_part, name="edit_part"),
    path('ecr/<int:ecr_number>/', cViews.ecr_detail, name="ecr_detail"),
    path('ecr/add/', cViews.ecr_add, name="add_ecr"),
    path('ecr/edit/<int:ecr_number>/', cViews.ecr_edit, name="ecr_edit"),
    path('ecr/', cViews.ecr_list, name="ecr_list"),
    path('utilities/upload/', cViews.file_upload, name="file_upload"),
    path('utilities/download/<str:path>', cViews.download, name="download"),
    path('rev/add/<str:drawing_number>/<int:ecr_number>/', cViews.revise_drawing, name="add_rev"),
    path('performance/', cViews.performance, name="performance"),
    path('project/', pViews.project_list, name="project_list"),
    path('project/<int:id>', pViews.project, name="project"),
    path('project/add/', pViews.add_project, name="add_project"),
    #path('download/projects/<str:path>', pViews.download_media, name="download"),
]
