#from django.shortcuts import render_to_response
from reservacionesapp32.forms import LoginForm
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.views import LoginView

#from reservacionesapp32.autenticador import authenticatez
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
#from . models import Usuarios
from django.shortcuts import get_object_or_404, render, redirect
from . forms import LoginForm
#from reservacionesapp32.settings import LOGIN_REDIRECT_URL
from django.views.decorators.cache import cache_control

from django.contrib.contenttypes.models import ContentType
from reservacionesapp32.autenticador import authenticatez

#from . filters import Filtrado


from django.core.cache import cache

from django.contrib import messages

from django.conf import settings

import json
import threading
from threading import Thread

from reservacionesapp32.models import Usuarios


def vista_login(request):

	
	is_authenticated = False

	if request.method == 'GET':
		context = LoginForm()
		return render (request, 'plantillas/login.html', {'form': context})

	if request.method == 'POST':
		q = Usuarios.objects.all()
	

		
#ahora se captura los datos desde el frontend FUNCIONA OK
		usuario_frontend = request.POST.get('nick', '')
		password_frontend = request.POST.get('password', '')	


# AHORA SE HACE EL FILTRADO

		x = q.filter(nick__iexact= usuario_frontend)

		# AHORA NECESITO A PARTIR DEL USUARIO FILTRADO, OBTENER SU PASSWORD
		# EN LA BD

		

		fila = get_object_or_404(x)


# con fila accedo a la contrasena del objeto x creado con get_object_...
		try:
			if x and password_frontend == fila.password:
				user = authenticatez(nick = x, password = fila.password)
				
				data = {}

				is_authenticated = True


				usuario_ready = is_authenticated

				name_user = x

				listado_permisos = {}

			# CREAR VARIABLE CON EL NOMBRE_USUARIO_SYS EN CACHE
	# AHORA HAY QUE CREAR EN LA CACHE UNA VARIABLE DONDE SE ALMACENE fila.nombre_usuario_sys
				variable_cache = cache.set('uno', fila.nick, None)


				#BLOQUE DE GRUPOS A CREAR
				g_administradores = Group.objects.get_or_create(name = 1)	
				g_usuarios_avanzados = Group.objects.get_or_create(name = 2)
				g_usuarios = Group.objects.get_or_create(name = 3)
				g_invitados = Group.objects.get_or_create(name = 4)	




				sw = ContentType.objects.get_for_model(Usuarios)
				# AQUI SE HACE LO DE LOS PERMISOS A LOS ROLES, CON fila.rol y un switch-case


				#INICIALIZAR UNA VARIABLE QUE TIENE ASIGNADO
				#UN ARREGLO VACIO	
				# LISTADO_PERMISOS = LISTADOP[PERM1, PERM2....] PERO VACIO

				# HACIENDO LOS PERMISOS
				#BLOQUE DE PERMISOS A CREAR
				
				#permiso1 = Permission.objects.create(codename = 'poder_hacer_busquedas', name='Poder buscar', content_type_id = 10)						
				#permiso2 = Permission.objects.create(codename = 'poder_crear_usuarios', name='Poder crear usuarios', content_type_id = 11)
				#permiso3 = Permission.objects.create(codename = 'poder_ver_detalles', name='Poder ver detalles', content_type_id = 12)



				# BLOQUE DONDE SE ASOCIAN LOS PERMISOS A LOS GRUPOS
				#g_usuarios.permissions = (permiso1, permiso3)
				#g_invitados.permissions = (permiso3)






				data['listax'] = fila  #aunque creo que en vez de x es fila
									# en realidad lo que va es el contexto, para
									# con listax acceder en la plantilla que indica
									# LOGIN_REDIRECT_URL	
			

				



				if is_authenticated and fila.rol == 1:

					tipo_de_rol = fila.rol
					quien_es = fila.nick
					#correo_usuario_actual = fila.correo

					
					request.session['selected_project_id'] = quien_es

					request.session['roleando'] = tipo_de_rol

				#	request.session['correo_usuario_actual'] = correo_usuario_actual
					#usuario_desde_cache = cache.get('uno')
					
					# PARA METER EN DATA LOS TIPO_DE_ROL_X, TAMBIEN 

					#perm1 = Permission.objects.create(codename = 'add_group', name= 'Can add group', content_type = 'Usuarios')

					#		return perm1, permx o hacer un arreglo y meter los PERMISOS
					#				en ese arreglo que pertenezca a data


					return redirect('/listarreservacion/')


					# O RETURN LISTADO_PERMISOS = LISTADOP[PERM1, PERM2....]




				elif is_authenticated and fila.rol == 2:


					tipo_de_rol = fila.rol
					quien_es = fila.nick
					#correo_usuario_actual = fila.correo

					data=dict()
					data['rule']=tipo_de_rol

					request.session['selected_project_id'] = quien_es

					request.session['roleando'] = tipo_de_rol

				#	request.session['correo_usuario_actual'] = correo_usuario_actual


					#		perm2 = Permission.objects.create(codename = 'add_group', name= 'Can add group', content_type = '')
					#
					# O RETURN LISTADO_PERMISOS = LISTADOP[PERM1, PERM2....]

					#return redirect('/avanzado/')

					return render(request, 'plantillas/avanzado.html', data)
					





				elif is_authenticated and fila.rol == 3:


					tipo_de_rol = fila.rol
					quien_es = fila.nick
					#correo_usuario_actual = fila.correo
					data=dict()
					data['rule_usuario']=tipo_de_rol
					
					request.session['selected_project_id'] = quien_es

					request.session['roleando'] = tipo_de_rol

					#request.session['correo_usuario_actual'] = correo_usuario_actual


					#return HttpResponseRedirect('/usuario/')
					return render(request, 'plantillas/usuario.html', data)





				elif is_authenticated and fila.rol == 4:

					#data['listq'] = fila
					tipo_de_rol = fila.rol
					quien_es = fila.nick
				#	correo_usuario_actual = fila.correo


					data=dict()
					data['rule_invitado']=tipo_de_rol

					
					request.session['selected_project_id'] = quien_es

					request.session['roleando'] = tipo_de_rol

					#request.session['correo_usuario_actual'] = correo_usuario_actual


					
					#return HttpResponseRedirect('/appprototipo/listarusuarios/')

					#return HttpResponseRedirect('/invitado/')
										
					return render(request, 'plantillas/invitado.html', data)



			


# CREAR UN CONTEXTO QUE CONTENGA usuario_ready (o is_authenticated), listado_permisos[], fila, la variable de cache
# y ademas tipo_de_rol (en la plantilla solo se pone tipo_d_rol, no hay que hacer asignacion alguna)
# y ademas quien_es (PARA LO DE BIENVENIDO(A), quien_es)


				
				return redirect(LOGIN_REDIRECT_URL, data)



			else:
				context = LoginForm()
				return render(request, 'plantillas/login.html', {'form': context})
		except Usuarios.DoesNotExist:	
			context = LoginForm()
			return render(request, 'plantillas/login.html', {'form': context})