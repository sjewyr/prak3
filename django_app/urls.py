from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
import socket

def health_check(request):
    """Health check endpoint для Kubernetes probes"""
    return JsonResponse({'status': 'healthy', 'hostname': socket.gethostname()})

def home(request):
    """Главная страница с информацией о pod"""
    from django.shortcuts import render
    return render(request, 'home.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', health_check, name='health'),
    path('', home, name='home'),
    path('metrics/', include('django_prometheus.urls')),
]
