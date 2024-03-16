from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
  
    path('userResgister/',views.userResgisterViews.as_view(),name='register'),
    path('active/<uid64>/<token>/',views.activete,name='activate'),
    path("login/",views.LoginAPIView.as_view(),name='login'),
    path('logout/',views.LogOutApiview.as_view(),name='logout'),
]
