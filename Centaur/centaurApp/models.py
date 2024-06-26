from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

#from Centaur.centaurApp.managers import UserAccountManager

# Create your models here.
#upload = models.ImageField(upload_to ='media/') 
class UserAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
   #"""Creates and saves a User with the given email, name and password."""
        if not email:
            raise ValueError('Users must have an email address')
                        
        email=self.normalize_email(email)
        email = email.lower()
        
        user = self.model(
            email=email,
            username=username
        )
       
        user.set_password(password)
        user.save(using=self._db)
        return user
        
    def create_admin(self, email, username, password=None):
        """
        Creates and saves a superuser with the given email, name and password.
        """
        user = self.create_user(email, username, password)
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user
            
    def create_superuser(self, email, username, password=None):
        """
        Creates and saves a superuser with the given email, name and password.
        """
        user = self.create_user(email, password,username)
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Usuario(AbstractBaseUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    username = models.CharField('username', max_length=100)
    #profile_picture = models.ImageField(upload_to ='media/% Y/% m/% d/', null=True, blank=True)
    nombre = models.CharField('nombre', max_length = 100)
    apellido = models.CharField('apellido', max_length = 200)
    email = models.EmailField('email', unique=True)
    password = models.CharField(max_length=50)
    search_fields = ("email")
    objects = UserAccountManager()


class Contenido(models.Model):
    nombre = models.CharField('nombre', max_length=100)
    valor = models.CharField('valor', max_length=500)
    def __str__(self):
       return '{0}'.format(self.nombre)

class Ticket(models.Model):
    ALTA = 'alta'
    MEDIA = 'media'
    BAJA = 'baja'
    ABIERTO = 'abierto'
    EN_CURSO = 'en_curso'
    CERRADO = 'cerrado'
    PRIORIDADES = [
        (ALTA, "Alta"), (MEDIA, "Media"), (BAJA, "Baja")
    ]
    ESTADO =[
        (ABIERTO, "Abierto"), (EN_CURSO, "En curso"), (CERRADO, "Cerrado")
    ]

    @classmethod
    def get_prioridad_choices(cls):
        return [choice[0] for choice in cls.PRIORIDADES]

    @classmethod
    def get_estado_choices(cls):
        return [choice[0] for choice in cls.ESTADO]
    
    titulo = models.CharField('Titulo', max_length = 100)
    descripcion = models.CharField('Descripcion', max_length = 100)
    contenido = models.ManyToManyField(Contenido, blank=True)
    solicitante = models.CharField('Solicitante', max_length = 100, blank=True)
    encargado = models.CharField('Encargado', max_length = 100, default='Sin asignar')
    prioridad = models.CharField(max_length=6, choices=PRIORIDADES, default=BAJA)
    estado = models.CharField(max_length=10, choices=ESTADO, default=ABIERTO)
   # encargado = models.ForeignKey(
   #     "Agente",
   #     on_delete=models.CASCADE,
   # )
    #solicitante = models.ForeignKey(
    #    "Usuario",
    #    on_delete=models.CASCADE,
    #)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_ini = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    conversacion = models.ForeignKey(
        "Chat",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    nota = models.CharField('Nota', max_length = 100, blank=True, null=True)
    carpeta = models.CharField('Carpeta', max_length = 100, blank=True,null=True)
    categoria = models.CharField('Categoria', max_length = 100, blank=True,null=True)
    def __str__(self):
        return '{0}'.format(self.titulo)


class Opcion(models.Model):
    nombre = models.CharField(max_length=100, blank=True)
    valor = models.CharField(max_length=100, null=True)
    def __str__(self):
        return '{0}'.format(self.nombre)

class Campo(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100, blank=True)
    opciones = models.ManyToManyField(Opcion, blank=True)
    def __str__(self):
        return '{0}'.format(self.nombre)


class Formulario(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=200)
    campos = models.ManyToManyField(Campo, blank=True)
    categoria = models.CharField(max_length=100, blank=True)
    oculto = models.BooleanField(default=True)
    def __str__(self):
        return '{0}'.format(self.titulo)





class Chat(models.Model):
    pass

class Nota(models.Model):
    pass


    
from django.contrib.auth import get_user_model    
User = get_user_model()   

from django.conf import settings
from datetime import datetime, time, date

def get_default_user():
    User = get_user_model()
    return User.objects.get_or_create(username='defaultuser')[0].id

class Tarea(models.Model):
    titulo = models.CharField('Titulo', max_length = 100)
    descripcion = models.CharField('Descripcion', max_length = 100)
    creador = models.CharField('Creador', max_length = 100)
    fecha_ini = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    hora_ini = models.TimeField(blank=True, null=True)
    hora_fin = models.TimeField(blank=True, null=True)
    def __str__(self):
        return '{0}'.format(self.titulo)

    