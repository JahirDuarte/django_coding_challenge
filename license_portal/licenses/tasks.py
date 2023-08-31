from __future__ import absolute_import, unicode_literals

from celery import shared_task
from datetime import datetime, date, timedelta
from typing import List, Any

# Django modules
from django.contrib.auth.models import User

# Apps modules
from licenses.notifications import AdminNotification, ClientNotification
from licenses.models import Client, License

@shared_task
def test_task():
    print ("Hello")
    return "Hello, I am a Test"


@shared_task
def task_admin_notifications():
    Notifications.admin_notifications()
    return True


@shared_task
def task_client_notifications():
    Notifications.client_notifications()
    return True


class Notifications:
    expiration_date = date.today()
    licenses = License.objects.all()

    four_months_date = expiration_date + timedelta(days=120)
    four_months_licenses = licenses.filter(expiration_datetime__lte=four_months_date)

    one_month_date = expiration_date + timedelta(days=30)
    one_month_licenses = licenses.filter(expiration_datetime__lte=one_month_date)

    one_week_date = expiration_date + timedelta(days=7)
    one_week_licenses = licenses.filter(expiration_datetime__lte=one_week_date)

    context = {
        'four_months_date': four_months_date,
        'one_month_date': one_month_date,
        'one_week_date': one_week_date,
        'four_months_licenses': [],
        'one_month_licenses': [],
        'one_week_licenses': [],
        'notification_type': ''
    }

    # Combine all licenses into a single queryset and extract unique clients
    all_licenses = four_months_licenses | one_month_licenses | one_week_licenses
    clients_with_licenses = all_licenses.values_list('client', flat=True).distinct()

    @classmethod
    def admin_notifications(self):
        notification = AdminNotification()
        admins = list(User.objects.filter(is_staff=True).values_list('email', flat=True))
        context = self.context

        for client_id in self.clients_with_licenses:
            client = Client.objects.get(id=client_id)
            licenses = self.all_licenses.filter(client=client)
            
            context['notification_type'] = 'admin'

            # create a list of licenses to render in the email template
            for license in licenses:
                license_data = {
                    'poc_contact_name': license.client.poc_contact_name,
                    'poc_contact_email': license.client.poc_contact_email,
                    'id': license.id,
                    'type': license.get_license_type,
                    'package_name': license.get_package_name,
                }

                if license in self.four_months_licenses:
                    context['four_months_licenses'].append(license_data)
                if license in self.one_month_licenses:
                    context['one_month_licenses'].append(license_data)
                if license in self.one_week_licenses:
                    context['one_week_licenses'].append(license_data)

        notification.send_notification(admins, context)

        return True

    @classmethod
    def client_notifications(self):
        notification = ClientNotification()

        for client_id in self.clients_with_licenses:
            client = Client.objects.get(id=client_id)
            licenses = self.all_licenses.filter(client=client)
            context = self.context
            context['recipient_name'] = client.client_name
            context['notification_type'] = 'client'
            context['all_licenses'] = list(licenses.values_list('id', flat=True))

            # create a list of licenses to render in the email template
            for license in licenses:
                license_data = {
                    'id': license.id,
                    'type': license.get_license_type,
                    'package_name': license.get_package_name,
                }
                if license in self.four_months_licenses:
                    context['four_months_licenses'].append(license_data)
                if license in self.one_month_licenses:
                    context['one_month_licenses'].append(license_data)
                if license in self.one_week_licenses:
                    context['one_week_licenses'].append(license_data)

            notification.send_notification([client.poc_contact_email], context)

        return True
    

