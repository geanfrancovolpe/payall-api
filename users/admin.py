from django.contrib import admin
from .models import CustomUser

# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):

    list_display = ["email", "first_name", "last_name", "phone"]
    class Meta:
        model = CustomUser
        fields = ('__all__')
