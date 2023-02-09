# Generated by Django 4.1.2 on 2023-02-09 20:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_customuser_contacts'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Última actualización')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_contact_set', to=settings.AUTH_USER_MODEL, verbose_name='Contacto')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_owner_set', to=settings.AUTH_USER_MODEL, verbose_name='Responsable')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='customuser',
            name='contacts',
            field=models.ManyToManyField(blank=True, related_name='user', through='users.ContactList', to=settings.AUTH_USER_MODEL, verbose_name='Contactos'),
        ),
    ]
