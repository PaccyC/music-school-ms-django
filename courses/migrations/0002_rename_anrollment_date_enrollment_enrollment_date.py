# Generated by Django 5.1.2 on 2024-11-26 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enrollment',
            old_name='anrollment_date',
            new_name='enrollment_date',
        ),
    ]
