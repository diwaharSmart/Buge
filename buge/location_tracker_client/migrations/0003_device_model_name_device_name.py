# Generated by Django 4.1.1 on 2022-12-06 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location_tracker_client', '0002_remove_device_id_alter_device_device_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='model_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='device',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
