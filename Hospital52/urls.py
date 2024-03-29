"""Hospital52 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from AppHospital52 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    
    path('user/', views.UserCreateView.as_view()),
    path('userd/', views.UserDetailView.as_view()),
    
    path('account/', views.GestionPerfil.as_view()),
    path('account/<int:pk>/', views.GestionDetailPerfil.as_view()),
    
    path('persalud/', views.GestionPerSalud.as_view()),
    path('persalud/<int:pk>/', views.GestionDetailPersonalSalud.as_view()),
    
    path('ciudad/', views.GestionCiudad.as_view()),
    path('ciudad/<int:pk>/', views.GestionDetailCiudad.as_view()),
    
    path('paciente/', views.GestionPaciente.as_view()),
    path('paciente/<int:pk>/', views.GestionDetailPaciente.as_view()),
   
    path('hisclinica/', views.GestionHisClinica.as_view()),
    path('hisclinica/<int:pk>/', views.GestionDetailHisClinica.as_view()),

    path('sigvitales/', views.GestionSignosVitales.as_view()),
    path('sigvitales/<int:pk>/', views.GestionDetailSignosVitales.as_view()),

     path('familiar/', views.GestionFamiliar.as_view()),


    

]
