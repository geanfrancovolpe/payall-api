from django.db import models
from django.contrib.auth.models import AbstractUser
from core.models import BaseModel

# Create your models here.

class ContactList(BaseModel):
    owner = models.ForeignKey(
        "users.CustomUser", 
        verbose_name=u"Responsable", 
        related_name="rel_owner_set",
        on_delete=models.CASCADE
    )
    contact = models.ForeignKey(
        "users.CustomUser", 
        verbose_name=u"Contacto", 
        related_name="rel_contact_set",
        on_delete=models.CASCADE
    )

class CustomUser(AbstractUser):
    phone = models.CharField(
        verbose_name="Número de teléfono",
        max_length=20,
        blank=True,
        null=True
    )
    profile_picture = models.ImageField(
        verbose_name="Imagen de perfil",
        upload_to="profile_images",
        null=True,
        blank=True
    )
    contacts = models.ManyToManyField(
        "self",
        through=ContactList,
        verbose_name=u"Contactos",
        blank=True
    )

    def __str__(self):
        return self.email
    
