Django Coding Challenge
=======================

This challenge is designed to test your Django and Python skills.

Requirements
============

- Completed using Python v3.10 and all code must be annotated with type hints from the standard library `typing` module.
- Runs on docker and the application can be started with a single command `docker-compose up`
- The running application can be reached in the browser at *[docker host]:8080*
- The application is delivered with a sufficient admin reachable at *[docker host]:8080/admin*
- Delivered as a public fork of this GitHub repository
- **Show us your work** through your commit history
- Unit test the django endpoints.
- Add the sample data you use.

Scenario
========

You are implementing part of an SDK licensing application used to permit clients to download the company's proprietary software. The sales team needs a feature which automatically notifies them when one of their client's licenses will expire (and thus prevent the client from using the associated package).

Task
====

A bare bones Django project is provided in the *license_portal* directory. Within the `licenses` application implement an email sending mechanism to notify the admin point of contact `licenses.Client.admin_poc` of their clients license `licenses.License` expiration times. The message must be sent to a clients admin point of contact only if the following conditions are met:

1) The client has licenses which expire in exactly 4 months
2) The client has licenses which expire within a month and today is monday
3) The client has licenses which expire within a week
4) All of the above

The email body must consist of a list of all a client's licenses which meet the above conditions and emails must only include details for a single client (e.g. a separate email for each client). The expiring licenses in the email body must include:

- license id
- license type
- name of the package
- expiration date
- poc information of the client (name and email address)

This job must be trigger-able via an HTTP POST request without authentication or csrf validation and must include a summary of notifications sent since the application started on the homepage.

Implement a logging mechanism that logs whenever an email is sent. This should have its own table and must log:
- When the email was sent
- License id

Add a endpoint that shows the most recent X emails sent where x is the provided number.



_Tip:_ Use django's builtin `django.core.mail.backends.locmem.EmailBackend`

_Bonus:_ Make a simple react frontend that shows the licenes and the logs. Using celery would also be a plus.

Restrictions
============

None! Use whatever tools / third party libraries you feel are necessary to complete the task.

Fork of: https://github.com/castlabs/django-coding-challenge


CHALLENGE STEPS DONE
Step 1: Run the repository locally.
Step 2: Test sending notifications.
Step 3: Send with data from the database.
Step 4: Add conditionals.
Step 5: Ready for both notifications from tasks.
Step 6: Create an "EmailsSentRegister" model to log alert sending.
Step 7: Create an endpoint in React to view the "EmailsNotifications" model.
Step 8: Install, configure, and run Celery.
Step 9: Execute tasks from the Django admin panel.
Step 10: Create a simple React interface displaying records from the "Alerts" model obtained via API.