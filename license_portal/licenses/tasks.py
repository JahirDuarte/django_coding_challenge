from licenses.notifications import AdminNotification, ClientNotification

def admin_notifications():
    """
        - We use class inheritance to take advantage of the same features
        - Only change the 'subject' email param and the template path
    """
    notification = AdminNotification()
    recipients = ['jahir.duarte.inf@gmail.com'] # Only for testing email
    context = {
        'recipient_name': 'Jahir Duarte',
        'expiration_date': '2023-09-30',
    }
    notification.send_notification(recipients, context)
    return True

def client_notifications():
    """
        - We use class inheritance to take advantage of the same features
        - Only change the 'subject' email param and the template path
    """
    notification = ClientNotification()
    recipients = ['jahir.duarte.inf@gmail.com'] # Only for testing email 
    context = {
        'recipient_name': 'Jahir Duarte',
        'expiration_date': '2023-09-30',
    }
    notification.send_notification(recipients, context)
    return True