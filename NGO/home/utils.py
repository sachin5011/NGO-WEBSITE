from django.core.mail import send_mail
from django.conf import settings

def receive_email_from_client(name,email, message):
    subject = f"New Message from {name}"

    send_mail(subject=subject,
              message=message,
              from_email=email,
              recipient_list=[settings.EMAIL_HOST_USER])
