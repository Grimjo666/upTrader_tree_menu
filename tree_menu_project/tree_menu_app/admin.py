from django.contrib import admin
from .models import TreeMenu


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent', 'url', 'name')


admin.site.register(TreeMenu, MenuItemAdmin)
