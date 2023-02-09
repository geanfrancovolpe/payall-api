from django.contrib import admin
from .models import Service, Category, Group, InvitedUser

# Register your models here.
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ["name", "user"]
    filter_horizontal = ["categories"]

    class Meta:
        model = Service
        fields = ('__all__')


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    
    filter_horizontal = ["users", "files"]

    class Meta:
        model = Group
        fields = ('__all__')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    class Meta:
        model = Category
        fields = ('__all__')


@admin.register(InvitedUser)
class InvitedUserAdmin(admin.ModelAdmin):

    class Meta:
        model = InvitedUser
        fields = ('__all__')