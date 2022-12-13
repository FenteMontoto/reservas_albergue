from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator
from ckeditor.fields import RichTextField
import re
from .managers import UserManager
# Create your models here.

class User(AbstractBaseUser,PermissionsMixin):
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    GENDER_CHOICES=(
        ('H','Hombre'),
        ('M','Mujer'),
        ('O','Otros'),
    )
    username = models.CharField("Nombre de susuario",max_length=10, unique=True)
    email = models.EmailField()
    nombre = models.CharField("Nombre", max_length=30)
    primer_apellido = models.CharField("Primer apellido", max_length=30)
    segundo_apellido  = models.CharField("Segundo apellido", max_length=30, blank=True)
    genero = models.CharField("Sexo", max_length=6, choices=GENDER_CHOICES, blank=True)
    fecha_nac = models.DateField("Fecha de nacimiento", auto_now=False, auto_now_add=False)
    telefono = models.CharField("Telephone",validators = [phoneNumberRegex], max_length = 16, unique = True, null = False, blank = False)
    # huespedes = models.IntegerField("Huespedes")
    # fecha_entrada = models.DateField("Fecha de entrada", auto_now=False, auto_now_add=False)
    # fecha_salida = models.DateField("Fecha de salida", auto_now=False, auto_now_add=False)
    # hora_llegada = models.DateTimeField("Hora estimada de llegada", auto_now=False, auto_now_add=False)
    # comentarios=RichTextField("Comentarios",blank=True, null=True,default="")
    # key_room = models.IntegerField("Select a Key Room")
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD='username'
    REQUIRED_FIELDS=['email','fecha_nac','telefono',]
    objects=UserManager()
    def get_short_name(self):
        return self.username
    
    def get_full_name(self):
        return self.nombre+" "+self.primer_apellido+" "+self.segundo_apellido