from django.contrib import admin

from .models import Employee,Device,AssetsReturn,Company

model_register = [Employee,Device,AssetsReturn,Company]

for model in model_register:
    admin.site.register(model)

