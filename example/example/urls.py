from django.contrib import admin
from django.urls import path
import app.views 
urlpatterns = [
    path("", app.views.home, name="home"),
    path("addresses/", app.views.show_addresses, name="addresses"),
    path("messages/", app.views.show_messages, name="messages"),
    path("entry/", app.views.save_entry, name="save_entry"),
    path('admin/', admin.site.urls),
]
