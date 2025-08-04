from django.contrib import admin
from .models import Menu



# Custom Admins
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name','description','price','created_at']


# Register your models here.
admin.site.register(Menu,MenuAdmin)