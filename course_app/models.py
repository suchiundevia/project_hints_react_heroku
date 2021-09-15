from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from account_app.models import Learner


class Category(models.Model):
    category_name = models.CharField(max_length=70)
    category_description = models.CharField(max_length=150)

    def __str__(self):
        return str(self.category_name)

    class Meta:
        verbose_name_plural = 'Categories'


class Course(models.Model):
    course_title = models.CharField(max_length=150, null=True)
    course_subject = models.CharField(max_length=250, null=True)
    course_description = models.TextField(null=True)
    course_price = models.IntegerField(default=0, null=True)
    course_post_date = models.DateTimeField(default=timezone.now)
    categories = models.ManyToManyField(Category)
    course_author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.course_title)

    class Meta:
        verbose_name_plural = 'Courses'


class Chapter(models.Model):
    chapter_title = models.CharField(max_length=150)
    chapter_description = models.CharField(max_length=150)
    chapter_resource_link = models.URLField(max_length=250)
    chapter_sequence = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, )

    def __str__(self):
        return str(self.chapter_title)

    class Meta:
        verbose_name_plural = 'Chapters'


class Lecture(models.Model):
    lecture_title = models.CharField(max_length=150)
    lecture_description = models.CharField(max_length=150)
    lecture_video = models.FileField(upload_to="lecture_videos", null=True)
    lecture_sequence = models.IntegerField()
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.lecture_title)

    class Meta:
        verbose_name_plural = 'Lectures'


class Enrollment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    learner = models.ForeignKey(Learner, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.course)

    class Meta:
        verbose_name_plural = 'Enrollments'


class EnrollmentNotification(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(default='Your enrolment is complete')
    notification_date = models.DateTimeField()
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.message)

    class Meta:
        verbose_name_plural = 'EnrollmentNotifications'
