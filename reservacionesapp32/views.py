

from __future__ import unicode_literals

#from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings

# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect, HttpResponse, HttpResponseRedirect
#from reservacionesapp.formulario_reg_usuario import UsuariosForm
from django.urls import *
from reservacionesapp32.models import Usuarios, Reservaciones
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


#from . serializers import usuarioSerializer
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers

import json

from reservacionesapp32.formulario_reservar import ReservacionesForm
from reservacionesapp32.formulario_reg_usuario import  UsuariosForm

from django.contrib.auth.models import Group, Permission

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.forms.models import model_to_dict


from django.views.generic.edit import UpdateView, BaseUpdateView



######################################################################################


#@login_required(login_url='login/')
def listarreservacionv(request, template_name='plantillas/listar_reservacion.html'):
	
	listadoreservacion = Reservaciones.objects.all().order_by('fecha_reservacion')
	
	#listadoreservacion = Reservaciones.objects.all()
	page = request.GET.get('page', 1)

	paginator = Paginator(listadoreservacion, 2)
	try:
		usersx = paginator.page(page)
	except PageNotAnInteger:
		usersx = paginator.page(1)
	except EmptyPage:
		usersx = paginator.page(paginator.num_pages)
	
	data = {}

	

	#data['lista'] = usersx
	data['lista'] = listadoreservacion


	return render(request, template_name, data)


################################################################################################

#@login_required(login_url='/login/')
def crearreservacionv(request, template_name='plantillas/crear_reservacion.html'):
	
	form = ReservacionesForm(request.POST)	
	
	if form.is_valid():
		#hashear(form.password)
		form.save()
	
	context =  {'form':form}	
	return render(request, template_name, context)

################################################################################################

'''

def reservacion_update(request, pk, template_name='plantillas/actualizacion_form.html'):

	reservacionactual= get_object_or_404(Reservaciones, pk=pk)

	form = ReservacionesForm(request.POST or None, instance=reservacionactual)

	if form.is_valid():

		reservacionactual.nombre_huesped=request.POST['nombre_huesped']
		reservacionactual.fecha_reservacion=request.POST['fecha_reservacion']


		reservacionactual.save()

		
		return redirect('listado_reservacion')
	else:
		form = ReservacionesForm(instance=reservacionactual)	
		
	return render(request, template_name, {'formx':form})'''

'''
def reservacion_update(request, pk):

	template_name='plantillas/actualizacion_form.html'

	reservacionactual=Reservaciones.objects.get(pk=pk)
	if request.method=="POST":
		form = ReservacionesForm(request.POST, instance=reservacionactual)
		if form.is_valid():
			form.nombre_huesped=request.POST['nombre_huesped']
			form.fecha_reservacion=request.POST['fecha_reservacion']


			form.save()

			return redirect('listado_reservacion')

	else:
		form=ReservacionesForm(instance=reservacionactual)
		ctx={'form':form}

	return render(request, template_name, ctx)	

'''

#@login_required(login_url='/login/')
def actual(request, pk):
	template_name='plantillas/actualizacion_form.html'

	reservacionactual=Reservaciones.objects.get(pk=pk)
	#reservacionactual=Reservaciones.objects.filter('nombre_huesped'=="pedroxy").update('nombre_huesped'=="pedruko")
	if request.method=="POST":
		form = ReservacionesForm(request.POST, instance=reservacionactual)
		
		if form.is_valid():
			
			form.save(commit=False)

			return redirect('listado_reservacion')

	else:
		form=ReservacionesForm(instance=reservacionactual)
	ctx={'form':form}



	return render(request, template_name, ctx)
		









'''
class ReservacionesActualizarUpdateView(UpdateView):
#		"""docstring for UsuariosActualizar"""


		model = Reservaciones
		fields=["fecha_reservacion", "nombre_huesped"]
		
		template_name = 'plantillas/actualizacion_form.html'
		success_url=reverse_lazy ('listado_reservacion')
'''

################################################################################################

#@login_required(login_url='/login/')
def borrar_reservacionv(request, pk):
	#listoparaborrar = Reservaciones.objects.filter(pk__startswith = pk)

	template_name='plantillas/borrar_reservacion.html'

	s = get_object_or_404(Reservaciones, pk=pk)
	
	data = dict()
	data['ds'] = s
	if request.method == 'POST':
		
	
		s.delete()
	

		return redirect('listado_reservacion')
	

	return render(request, template_name, data) 	
		
################################################################################################

def registrar_usuariov(request, template_name='plantillas/crear_login.html'):
	
	
	form = UsuariosForm(request.POST)	
	
	if form.is_valid():
		#hashear(form.password)

		form.save()

	
	context =  {'form':form}	
	return render(request, template_name, context)