from django.contrib import admin
from . import models

# Apps modules
from licenses.models import Client, License

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