from django.contrib import admin
from skus import models

# Register your models here.

class ClientAdmin(admin.ModelAdmin):
    ordering = ['shop']

admin.site.register(models.Client, ClientAdmin)