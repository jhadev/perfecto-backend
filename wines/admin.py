from django.contrib import admin
from .models import Wine

# Register your models here.


class WineAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Wine, WineAdmin)