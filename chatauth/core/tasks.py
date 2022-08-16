from celery import shared_task
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.mail import send_mail

from chatauth import settings
from chatauth.core.models import EmailNotification


@shared_task(bind=True)
def send_mail_func(self):
    users = get_user_model().objects.all()
    for user in users:
        main_subject = EmailNotification.message
        message = 'This is a simple Celery scheduled email'
        to_email = user.email
        send_mail(
            subject= main_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=True,
        )
    return 'Done'
