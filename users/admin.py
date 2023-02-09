from django.contrib import admin
from .models import CustomUser, ContactList

# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):

    list_display = ["email", "first_name", "last_name", "phone"]
    class Meta:
        model = CustomUser
        fields = ('__all__')


@admin.register(ContactList)
class ContactListAdmin(admin.ModelAdmin):

    list_display = ["owner", "contact", "created_at"]
    class Meta:
        model = ContactList
        fields = ('__all__')
