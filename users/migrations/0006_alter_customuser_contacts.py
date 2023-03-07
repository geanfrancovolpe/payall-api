# Generated by Django 4.1.2 on 2023-02-12 11:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_contactlist_customuser_contacts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='contacts',
            field=models.ManyToManyField(blank=True, through='users.ContactList', to=settings.AUTH_USER_MODEL, verbose_name='Contactos'),
        ),
    ]