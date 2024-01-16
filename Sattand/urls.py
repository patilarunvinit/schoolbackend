from django.urls import path
from . import views

urlpatterns=[
    path('attandForS/', views.attandForS),
    path('attandcheck/', views.checkback),
    path('tfilterstand/', views.Tfiltertostand),
    path('tfilterdate/', views.Tfiltertodate),
    path('Sattendence/', views.Sattendence),
    path('percentageCAl/', views.percentageCAl),

]