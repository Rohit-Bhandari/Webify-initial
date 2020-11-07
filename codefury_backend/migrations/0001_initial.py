# Generated by Django 3.1.3 on 2020-11-07 08:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_no', models.IntegerField(default=0)),
                ('education', models.CharField(default='', max_length=100)),
                ('adhaar_number', models.IntegerField(default=0, unique=True)),
                ('salary_expected', models.IntegerField(default=0)),
                ('previous_job', models.CharField(default='', max_length=100)),
                ('skills', models.CharField(default='', max_length=100)),
                ('languages_known', models.CharField(default='', max_length=100)),
                ('living_location', models.CharField(default='', max_length=100)),
                ('working_hours', models.CharField(choices=[('F', 'Full Time'), ('P', 'Part time')], default='', max_length=100)),
                ('shift', models.CharField(choices=[('M', 'Morning'), ('E', 'Evening')], default='', max_length=100)),
                ('points', models.IntegerField(default=0)),
                ('recommended_user', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_type', models.CharField(default='', max_length=100)),
                ('jobs_number', models.IntegerField(default=0)),
                ('salary', models.IntegerField(default=0)),
                ('minimum_qualification', models.CharField(default='', max_length=100)),
                ('minimum_experience', models.IntegerField(default=0)),
                ('languages_required', models.CharField(default='', max_length=100)),
                ('job_location', models.CharField(default='', max_length=100)),
                ('job_hours', models.CharField(choices=[('F', 'Full Time'), ('P', 'Part time')], default='', max_length=100)),
                ('job_shift', models.CharField(choices=[('M', 'Morning'), ('E', 'Evening')], default='', max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
