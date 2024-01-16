from django.urls import path
from . import views

urlpatterns=[
    path('complaintForm/', views.complaintForm),
    path('teacherComp/', views.teacherComp),
    path('ComDeleteById/', views.ComDeleteById),

]