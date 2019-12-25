from django.contrib import admin
from store import models
# Register your models here.

admin.site.register(models.Storesetting)
admin.site.register(models.Product)
admin.site.register(models.Customer)
admin.site.register(models.CustomerCart)
admin.site.register(models.Address)
admin.site.register(models.Order)
