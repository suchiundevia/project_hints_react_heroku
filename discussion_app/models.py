from django.db import models
from account_app.models import Learner
from django.contrib.auth.models import User


class TimeSlot(models.Model):
    time = models.TimeField()
    date = models.DateTimeField(blank=True, null=True)
    booked = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name_plural = 'TimeSlots'


class Meeting(models.Model):
    meeting_title = models.CharField(max_length=150, null=True)
    meeting_status = models.CharField(max_length=150, null=True)
    meeting_description = models.TextField(null=True)
    time_slot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE, null=True)
    learner = models.ForeignKey(Learner, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.meeting_title)

    class Meta:
        verbose_name_plural = 'Meetings'
