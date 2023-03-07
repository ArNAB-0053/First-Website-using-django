from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
   path("", views.index, name='Home'),
   path("about", views.about, name='About'),
   path("contactMe", views.contactMe, name='Contact Me'),
   path("python", views.python, name='Pyhton'),
   path("java", views.java, name='Java'),
   path("other", views.other, name='Others'),
]