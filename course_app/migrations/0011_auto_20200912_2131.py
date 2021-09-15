# Generated by Django 3.1 on 2020-09-12 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0010_auto_20200912_2107'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='lecture_video',
            field=models.FileField(null=True, upload_to='lecture_videos'),
        ),
        migrations.AlterField(
            model_name='enrollmentnotification',
            name='notification_date',
            field=models.DateTimeField(),
        ),
    ]