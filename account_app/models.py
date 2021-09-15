from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, default="", on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pictures')
    about = models.CharField(max_length=250, null=True, blank=True)
    qualification = models.CharField(max_length=200, null=True, blank=True)
    experience = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.about} UserProfile'

    class Meta:
        verbose_name_plural = 'User Profile'


class Instructor(models.Model):
    user = models.OneToOneField(User, default="", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name_plural = 'Instructor'


class Learner(models.Model):
    user = models.OneToOneField(User, default="", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name_plural = 'Learner'
