# Generated by Django 5.1.4 on 2024-12-09 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TA_Scheduler', '0006_alter_course_course_instructor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_instructor',
            field=models.CharField(max_length=50, null=True),
        ),
    ]