"""discografia URL Configuration

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
from disco.views import list_disco, new_disco, delete_disco, update_disco

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list_disco/', list_disco, name='list_disco'),
    path('new_disco/', new_disco, name='new_disco'),
    path('delete_disco/<int:pk>/', delete_disco, name='delete_disco'),
    path('update_disco/<int:pk>/', update_disco, name='update_disco'),
]
