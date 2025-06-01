from django.contrib import admin
from django.urls import path

from .views import home_page_view

urlpatterns = [
    path("", home_page_view, name="home"),  # Root URL
    path("home/", home_page_view),          # Optional secondary route
    path("admin/", admin.site.urls),
]
