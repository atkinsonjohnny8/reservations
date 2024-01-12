from django import forms
from reservacionesapp32.models import Usuarios

class LoginForm(forms.Form):
	nick = forms.CharField(max_length = 30)
	password=forms.CharField(widget=forms.PasswordInput())


	class Meta:
	        model = Usuarios
	        fields = ('nick', 'password' )