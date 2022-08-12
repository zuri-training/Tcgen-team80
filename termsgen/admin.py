from django.contrib import admin

from .models import database, signUp

# Register your models here.


from .models import basic


admin.site.register(basic)


admin.site.register(database)
admin.site.register(signUp)
