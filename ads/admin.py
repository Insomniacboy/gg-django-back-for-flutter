from django.contrib import admin

# Register your models here.
from .models import Image, Info

class ImageAdmin(admin.StackedInline):
    model = Image

class InfoAdmin(admin.ModelAdmin):
    inlines = [ImageAdmin]

    class Meta:
        model = Info

admin.site.register(Info, InfoAdmin)
admin.site.register(Image)