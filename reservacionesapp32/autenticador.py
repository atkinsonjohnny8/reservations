from . models import Usuarios
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import check_password
import logging
#import appprototipo.view_login
import threading
from threading import Thread



	


def authenticatez(nick, password):

	try:
				
		#user = get_object_or_404(Usuarios, pk = pk)
		user = Usuarios()
		
		#user = Usuarios.objects.filter(nombre_usuario_sys = user.nombre_usuario_sys)
		usuario_auth = Usuarios.objects.filter(nick__startswith = '')	
		password_auth = Usuarios.objects.filter(password__startswith = '')		
		if user.check_password(password_auth):
			return user
		else:
			return HttpResponse ("Usuario o Password incorrecto")
			#return None
	except Usuarios.DoesNotExist:
			return HttpResponse ("No hay usuarios todavia")