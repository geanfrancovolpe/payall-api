from django.db import models
from core.models import BaseModel
from .constants import CURRENCY_USD, CURRENCIES
from users.models import CustomUser

class Category(BaseModel):
    name = models.CharField(
        verbose_name="Nombre del servicio",
        blank=False,
        null=False,
        max_length=1000
    )

    def __str__(self):
        return self.name


    
class Service(BaseModel):
    name = models.CharField(
        verbose_name="Nombre del servicio",
        blank=False,
        null=False,
        max_length=1000
    )
    user = models.ForeignKey(
        CustomUser,
        related_name=u"service",
        on_delete=models.CASCADE,
        verbose_name=u"Responsable",
        null=False,
        blank=False
    )
    categories = models.ManyToManyField(
        Category,
        verbose_name=u"Categorías",
        related_name="services",
        blank=True,
    )

    def __str__(self):
        return self.name



class Group(BaseModel):
    title = models.CharField(
        verbose_name="Título del grupo",
        blank=False,
        null=False,
        max_length=1000
    )
    service = models.ForeignKey(
        Service,
        related_name=u"assoc_groups",
        verbose_name=u"Servicio asociado",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    user = models.ForeignKey(
        CustomUser,
        related_name=u"created_groups",
        verbose_name=u"Responsable",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    currency = models.IntegerField(
        verbose_name=u"Divisa",
        default=CURRENCY_USD,
        choices=CURRENCIES
    )
    payment_date = models.DateField(
        verbose_name=u"Fecha de cobro",
        null=True,
        blank=True
    )
    amount = models.FloatField(
        default=0,
        verbose_name="Monto"
    )
    files = models.ManyToManyField(
        "files.MediaFile",
        verbose_name=u"Archivos",
        blank=True,
        related_name="files",
    )
    users = models.ManyToManyField(
        CustomUser,
        related_name=u"assoc_groups",
        verbose_name=u"Usuarios asociados",
        blank=True
    )

    def __str__(self):
        return self.title