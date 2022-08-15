import imp
from multiprocessing.spawn import import_main_path
from typing import OrderedDict
from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Customer)
