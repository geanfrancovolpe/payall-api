from django.db import models
from users.models import CustomUser

# Create your models here.
class MediaFile(models.Model):

    name = models.CharField(
        verbose_name=u"Nombre de referencia", max_length=150, blank=True, null=True
    )
    media_file = models.FileField(verbose_name=u"Fichero", upload_to="media")
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name=u"Usuario creador",
        null=True,
        blank=True
    )
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"Media file"
        verbose_name_plural = u"Media files"
