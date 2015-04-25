from django.contrib import admin

# Register your models here.

from models import Pages
from models import Css

admin.site.register(Css)

admin.site.register(Pages)
