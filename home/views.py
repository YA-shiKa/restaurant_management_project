from django.shortcuts import render
from product.models import Menu
def home(request):
    menu_items=Menu.objects.all()
    return render(request,'home/home.html',{'menu_items':menu_items})

