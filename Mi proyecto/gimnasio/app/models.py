from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class Plan(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

opciones_consultas = [
    [0, "consulta"],
    [1, 'Reclamo'],
    [2, 'Sugerencia'],
    [3, 'Otros'],
]
class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField(max_length=50)
    def __str__(self):
        return self.nombre
    
class UsuarioManager(BaseUserManager):
    def create_user(self, email, nombre, password=None, tipo_usuario='cliente'):
        if not email:
            raise ValueError('El email debe ser proporcionado')
        email = self.normalize_email(email)
        user = self.model(email=email, nombre=nombre, tipo_usuario=tipo_usuario)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nombre, password=None):
        user = self.create_user(email, nombre, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    

class Usuario(AbstractBaseUser):
    TIPO_USUARIO_CHOICES = (
        ('cliente', 'Cliente'),
        ('personal', 'Personal del Gimnasio'),
    )

    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=100)
    tipo_usuario = models.CharField(max_length=10, choices=TIPO_USUARIO_CHOICES, default='cliente')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre']

    objects = UsuarioManager()

    def __str__(self):
        return self.nombre





