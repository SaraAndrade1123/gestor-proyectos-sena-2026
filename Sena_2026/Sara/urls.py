
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',lambda request: HttpResponse("¡Hola mundo desde Django!")),
    path('acerca-de/', views.about_us),
]
