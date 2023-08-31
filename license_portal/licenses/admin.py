from django.contrib import admin
from . import models

# Apps modules
from licenses.models import Client, License, EmailsSentRegister

# Register your models here.
@admin.register(models.Client)
class ClientAdmin(admin.ModelAdmin):
	list_display = [
		'client_name',
		'poc_contact_name',
		'poc_contact_email'
	]

@admin.register(models.License)
class LicenseAdmin(admin.ModelAdmin):
    list_display = [
        'client',
        'package',
        'license_type',
        'expiration_datetime'
    ]

@admin.register(models.EmailsSentRegister)
class EmailsSentRegisterAdmin(admin.ModelAdmin):
    list_display = [
        'email_delivery_dt',
        'licenses',
    ]