from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    phone = models.CharField(
        verbose_name="Número de teléfono",
        max_length=20,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.email