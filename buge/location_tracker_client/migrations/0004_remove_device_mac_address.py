# Generated by Django 4.1.1 on 2022-12-06 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location_tracker_client', '0003_device_model_name_device_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='mac_address',
        ),
    ]
