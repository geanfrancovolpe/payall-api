from django.contrib import admin
from .models import MediaFile

# Register your models here.
@admin.register(MediaFile)
class MediaFileAdmin(admin.ModelAdmin):
    
    class Meta:
        model = MediaFile
        fields = ('__all__')