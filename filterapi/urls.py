from django.urls import path
from . import views

urlpatterns=[
    path('ststudends/', views.test1),
    path('SFilterByStand/', views.SFilterByStand),

]