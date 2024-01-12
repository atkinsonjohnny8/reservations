

from django import forms
from reservacionesapp32.models import Reservaciones

from django.forms import widgets


class ReservacionesForm(forms.ModelForm):
	
	class Meta:
		model = Reservaciones
		fields = [
			'fecha_reservacion',
			'nombre_huesped',
			
		]

		labels = {

			'fecha_reservacion': 'Fecha de reservacion',
			'nombre_huesped': 'Nombre del huesped',
			
		}	
		
		widgets = {
			'fecha_reservacion': forms.TextInput(attrs={'class': 'form = control', 'id': 'reservacion_id', 'required': True, 'placeholder': 'Fecha'}),
			'nombre_huesped': forms.TextInput(attrs={'class': 'form = control', 'id': 'nombrehuesped', 'required': True, 'placeholder': 'Nombre del huesped...'}),
			

					
		}