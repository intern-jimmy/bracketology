from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bracket', views.multiBracket, name='bracket'),
    path('vinny', views.vinnyBracket, name="Vinny")
]
