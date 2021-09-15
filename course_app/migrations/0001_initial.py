# Generated by Django 3.1 on 2020-09-10 00:22

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account_app', '0003_auto_20200910_0022'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=70)),
                ('category_description', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(max_length=150)),
                ('course_subject', models.TextField()),
                ('course_description', models.CharField(max_length=250)),
                ('course_price', models.IntegerField(default=0)),
                ('course_post_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('categories', models.ManyToManyField(to='course_app.Category')),
                ('course_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account_app.instructor')),
            ],
        ),
    ]
