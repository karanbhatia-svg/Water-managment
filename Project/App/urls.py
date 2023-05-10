from django.urls import path
from . import views


urlpatterns = [
path('', views.form, name='form'),
path('calculate', views.calculate, name='calculate'),


]