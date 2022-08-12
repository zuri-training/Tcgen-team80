from django.contrib import admin

# Register your models here.

from .models import basic,signup


admin.site.register(basic)
admin.site.register(signup)