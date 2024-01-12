
from django import forms
from reservacionesapp32.models import Usuarios

from django.forms import widgets




class UsuariosForm(forms.ModelForm):
	
	class Meta:
		model = Usuarios
		fields = [
			'nombre_usuario',
			'nick',
			'password',
			'rol',
			'sexo',
		]
		labels = {

			'nombre': 'Username',
			'nick': 'Nickname',
			'password': 'User password',
			'rol': 'User role',
			'sexo': 'User gender',
			
			
		}	
		
		widgets = {
			'nombre': forms.TextInput(attrs={'class': 'form = control', 'id': 'nombre', 'required': True, 'placeholder': 'Type name...'}),
			'nick': forms.TextInput(attrs={'class': 'form = control', 'id': 'nick', 'required': True, 'placeholder': 'Type nickname...'}),
			'password': forms.PasswordInput(attrs={'class': 'form = control','required': True, 'placeholder': 'Type your password...'}),
			'rol': forms.Select(attrs={'class': 'form = control', 'id': 'rol_id','required': True, 'placeholder': 'Permiso...'}),
			'sexo': forms.Select(attrs={'class': 'form = control', 'id': 'sexo_id','required': True, 'placeholder': 'Sexo...'}),
					
		}