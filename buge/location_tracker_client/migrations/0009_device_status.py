# Generated by Django 4.1.1 on 2022-12-12 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location_tracker_client', '0008_location_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='status',
            field=models.CharField(choices=[('running', 'running'), ('uninstall', 'uninstall')], default='running', max_length=255),
        ),
    ]