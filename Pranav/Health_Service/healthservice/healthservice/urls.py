from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('health/', include('healthApp.urls')),
    path('admin/', admin.site.urls),
]