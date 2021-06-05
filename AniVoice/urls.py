from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('Voicer.urls')),
    path('admin/', admin.site.urls),
]
