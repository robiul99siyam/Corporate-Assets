from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("assets_app_tracker.urls")),
    path('authentication/',include("user.urls")),
]
