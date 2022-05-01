from django.contrib import admin

# Register your models here.
from .models import Info, SubInfo
admin.site.register(Info)
admin.site.register(SubInfo)