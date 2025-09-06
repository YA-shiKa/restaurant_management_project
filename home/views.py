from django.shortcuts import render
from .models import Restaurant
import requests
def homepage(request):
    response=requests.get('http://127.0.1.8000'/api/menu/')
    if response.status_code==200:
        menu=response.json()
    else:
        menu=[]
    return render(request,'home/homepage.html',{'menu':menu})