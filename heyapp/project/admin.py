from django.contrib import admin
from .models import photos,categories,location

# Register your models here.

admin.site.register(location)
admin.site.register(photos)
admin.site.register(categories)
