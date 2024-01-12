from django.db import models
#from django.contrib.auth.models import AbstractBaseUser



# Create your models here.
class Reservaciones(models.Model):

	
	nombre_huesped = models.CharField(max_length=255, primary_key=True)
	fecha_reservacion = models.DateField(blank=True, null=True)
	
	def __str__():
		self.nombre_huesped	
		self.fecha_reservacion
	
	


class Usuarios (models.Model):
	"""docstring for Usuarios"""
	MASCULINO = 1
	FEMENINO = 2
	SEXO=(
		(MASCULINO, 'Man'),
		(FEMENINO, 'Woman'),
		)
	
	ADMINISTRADOR = 1
	USUARIO_AVANZADO = 2
	USUARIO = 3
	INVITADO = 4

	ROL=(
		(ADMINISTRADOR, 'Administrators'),
		(USUARIO_AVANZADO, 'Avanced users'),
		(USUARIO, 'Common user'),
		(INVITADO, 'Guest'),
		)

	
	
	nombre_usuario=	models.CharField(max_length=255, primary_key=True)
	nick = models.CharField(max_length=255)

	

	sexo = models.PositiveSmallIntegerField(choices=SEXO, blank=True, null=True)
	
	#nombre_usuario_sys = models.CharField(max_length=30)
	rol= models.PositiveSmallIntegerField(choices=ROL, blank=True, null=True)
	password = models.CharField(max_length=255)
	#fecha_creacion_usuario = models.DateTimeField(default=datetime.datetime.now)
	#is_staff = models.NullBooleanField()
    #	is_active = models.NullBooleanField(default=True)
    
    #	objects = MyUserManager()


	#USERNAME_FIELD = 'nombre_usuario'
	#USERNAME_FIELD = 'nick'
	#REQUIRED_FIELDS = ['nombre', 'apellido', 'correo', 'sexo', 'rol', 'password']


	#def get_absolute_url(self):
	#	return reverse('detalle_usuario', kwargs={'pk': self.pk})


	def check_password(self, password):
		return True
		if self.password == password:
			return True

	def __str__():
		self.nombre_usuario	
		self.nick
		self.sexo
		self.rol
		self.password