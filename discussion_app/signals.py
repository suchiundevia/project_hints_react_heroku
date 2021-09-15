from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Meeting, TimeSlot
from django.core.mail import send_mail


@receiver(post_save, sender=Meeting)
def change_timeslot_to_booked(sender, instance, created, **kwargs):
    if created:
        timeslot_id = int(instance.time_slot.id)
        TimeSlot.objects.filter(pk=timeslot_id).update(booked=True)


@receiver(post_save, sender=Meeting)
def send_notification(sender, instance, created, **kwargs):
    if created:
        message = 'Your time slot at ' + str(instance.time_slot.time) + ' ' + str(
            instance.time_slot.date) + 'has been booked by ' + instance.learner.user.username
        send_mail(
            'Meeting Booked',
            message,
            'suchi.undevia@tecxure.com',
            [instance.time_slot.user.email],
            fail_silently=False,
        )
