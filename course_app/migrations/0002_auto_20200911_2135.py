# Generated by Django 3.1 on 2020-09-11 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter_title', models.CharField(max_length=150)),
                ('chapter_description', models.CharField(max_length=150)),
                ('chapter_resource_link', models.URLField(max_length=250)),
                ('chapter_sequence', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='course',
            name='course_description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_subject',
            field=models.CharField(max_length=250),
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lecture_title', models.CharField(max_length=150)),
                ('lecture_description', models.CharField(max_length=150)),
                ('lecture_sequence', models.IntegerField()),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_app.chapter')),
            ],
        ),
        migrations.AddField(
            model_name='chapter',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_app.course'),
        ),
    ]
