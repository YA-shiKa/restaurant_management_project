from django.urls import path
from .views import *

urlpatterns = [
    path('menu/',MenuView.as_view(),name='menu'),
]