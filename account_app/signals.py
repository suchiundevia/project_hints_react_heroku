from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserProfile, Learner
from django.core.mail import send_mail
from account_app.tasks import send_signup_email_task


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    print('User saved in database')
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()


@receiver(post_save, sender=User)
def send_email(sender, instance, created, **kwargs):
    if created:
        recipient = instance.email
        send_signup_email_task.delay(recipient)


@receiver(post_save, sender=User)
def create_learner(sender, instance, created, **kwargs):
    if created:
        Learner.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_learner(sender, instance, **kwargs):
    instance.learner.save()
