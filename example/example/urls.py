from django.contrib import admin
from django.urls import path
import app.views 
urlpatterns = [
    path("", app.views.home, name="home"),
    path('admin/', admin.site.urls),
]
