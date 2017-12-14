from django.contrib import admin
from . import models

admin.site.register(models.User)
admin.site.register(models.Store)
admin.site.register(models.Image)

# Register your models here.
