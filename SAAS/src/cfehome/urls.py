from django.contrib import admin
from django.urls import path

from .views import home_view
from .views import about_view

urlpatterns = [
    path("", home_view, name="home"),  # Root URL
    path("about", about_view, name="home"),  # Root URL
    
    path("home/", home_view),          # Optional secondary route
    path("admin/", admin.site.urls),
]
