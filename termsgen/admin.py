from django.contrib import admin
from .models import basic,signUp,Customer

# Register your models here.

admin.site.register(basic)
admin.site.register(Customer)
admin.site.register(signUp)
