from django.contrib import admin
from django.urls import path
from core.views import index, nome

urlpatterns = [
    path('', index),
    path('nome/', nome),
    path('admin/', admin.site.urls),
]
