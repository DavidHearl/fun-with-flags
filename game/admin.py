from django.contrib import admin
from .models import Flag


@admin.register(Flag)
class FlagAdmin(admin.ModelAdmin):
    list_display = ('flag', 'programatic_name', 'image', 'fact', 'creation_date', 'difficulty')
    prepopulated_fields = {'programatic_name': ('flag',)}

