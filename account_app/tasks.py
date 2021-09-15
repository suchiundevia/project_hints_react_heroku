from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_signup_email_task(recipient):
    message = 'Welcome to Hints! Browse through courses or book discussion time with other members'
    send_mail(
        'Hints Project Sign-Up!',
        message,
        'suchi.undevia@tecxure.com',
        [recipient],
        fail_silently=False,
    )
