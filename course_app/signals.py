from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import EnrollmentNotification, Enrollment
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.core.mail import send_mail


@receiver(post_save, sender=Enrollment)
def create_enrollment_notification(sender, instance, created, **kwargs):
    if created:
        learner_id = instance.learner.id
        user = get_object_or_404(User, id=learner_id)
        EnrollmentNotification.objects.create(recipient=user,
                                              message='You have been enrolled in ' + instance.course.course_title,
                                              notification_date=timezone.now(),
                                              enrollment=instance)


@receiver(post_save, sender=EnrollmentNotification)
def send_enrollment_notification(sender, instance, created, **kwargs):
    if created:
        send_mail(
            'Enrollment Notification',
            instance.message,
            'suchi.undevia@tecxure.com',
            [instance.recipient.email],
            fail_silently=False,
        )
