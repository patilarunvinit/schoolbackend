from django.urls import path
from . import views

urlpatterns=[
    path('sutdinfo/', views.stinfo),
    path('slogin/', views.loginS),
    path('slogindata/', views.slogindataapi),
    path('slogout/', views.slogout),

]