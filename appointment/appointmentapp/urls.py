
from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("booking/",views.booking),
    path("form/",views.form),
    path("entryform/",views.entryform),





]