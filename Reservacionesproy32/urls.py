"""Reservacionesproy32 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from reservacionesapp32.views import listarreservacionv, crearreservacionv, borrar_reservacionv, actual, registrar_usuariov
from reservacionesapp32.view_login import vista_login


urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', vista_login, name = 'loginin'),
    path('registrarusuario/', registrar_usuariov, name='registrar'),

    path('avanzado/', vista_login, name = 'login_dos'),
    path('usuario/', vista_login, name = 'login_tres'),
    path('invitado/', vista_login, name = 'login_cuatro'),


    path('listarreservacion/', listarreservacionv, name = 'listado_reservacion'),
    path('crearreservacion/', crearreservacionv, name = 'crear_reservacion'),
    path('actualizarreservacion/<pk>', actual, name = 'actualizar_reservacion'),
    path('borrarreservacion/<pk>', borrar_reservacionv, name = 'borrar_reservacion'),

   

    
]
