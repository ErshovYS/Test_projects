from django.contrib import admin
from test_app import models

admin.site.register(models.OrderModel)
admin.site.register(models.PhoneModel)