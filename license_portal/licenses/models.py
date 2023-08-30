""" Data model for licenses application
"""
import enum

from datetime import timedelta, datetime
from typing import Tuple, List

from django.contrib.auth.models import User
from django.db import models

LICENSE_EXPIRATION_DELTA = timedelta(days=90)


def get_default_license_expiration() -> datetime:
    """Get the default expiration datetime"""
    return datetime.utcnow() + LICENSE_EXPIRATION_DELTA


class License(models.Model):
    """ Data model for a client license allowing access to a package
    """
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    package_choices = [
        (0, 'Javascript SDK'),
        (1, 'iOS SDK'),
        (2, 'Android SDK'),
    ]
    package = models.PositiveSmallIntegerField(choices=package_choices)
    license_type_choices = [
        (0, 'Production'),
        (1, 'Evaluation'),
    ]
    license_type = models.PositiveSmallIntegerField(choices=license_type_choices)

    created_datetime = models.DateTimeField(auto_now=True)
    expiration_datetime = models.DateTimeField(default=get_default_license_expiration)

    def get_license_type(self):
        if self.package == 0:
            return 'Production'
        elif self.package == 1:
            return 'Evaluation'
        return None

    def get_package_name(self):
        if self.package == 0:
            return 'Javascript SDK'
        elif self.package == 1:
            return 'iOS SDK'
        elif self.package == 2:
            return 'Android SDK'
        return None

class Client(models.Model):
    """ A client who holds licenses to packages
    """
    client_name = models.CharField(max_length=120, unique=True)
    poc_contact_name = models.CharField(max_length=120)
    poc_contact_email = models.EmailField()

    admin_poc = models.ForeignKey(User, limit_choices_to={'is_staff': True}, on_delete=models.CASCADE)

    def __str__(self):
        return self.poc_contact_email
