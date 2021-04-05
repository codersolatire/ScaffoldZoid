from django.contrib import admin
from .views import *
from django.urls import path, include

urlpatterns = [
    path('login/', login),
    path('logout/', logout),
    path('register/', register),
    path('profile/', profile),
    path('edit_profile/', edit_profile),
    path('', dashboard),
    path('save_orange/', save_orange),
    path('orange_list/', orange_list),
    path('seller_list/', seller_list),
    path('update_orange/', update_orange),
]
