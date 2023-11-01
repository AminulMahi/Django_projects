"""
URL configuration for inn_portfolio project.

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

from . import views

urlpatterns = [
    
    path('', include('adminapp.urls'))
    # path('admin/', admin.site.urls),
    # path('', views.index, name='index'),
    # path('admin/', views.admin_index, name='admin_index'),
    # path('user/', views.user, name='user_index'),
    # path('update/<str:id>', views.update, name='update_index'),
    # path('delete/<str:id>', views.delete, name='delete_item')
]
