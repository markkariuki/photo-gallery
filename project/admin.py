from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import photos,categories,location

admin.site.register(location)
admin.site.register(photos)
admin.site.register(categories)
