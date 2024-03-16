from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views



router = DefaultRouter()
router.register("device",views.DeviceViewSets)
router.register("assets/return",views.AssetsReturnViewSets)
router.register("employee/add/assets",views.EmployeeviewSets)
router.register("company",views.companyViewSets)

urlpatterns = [
  
  path("",include(router.urls)),
]
