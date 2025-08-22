from django.contrib import admin
from .models import Menu,Order
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display=('menu','description','price')
    search_fields=('name',)
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=('menu_item','quantity','order_date','total_price')
    list_filter=('order_date',)
    search_fields=('menu_item__name')