# Generated by Django 4.1.1 on 2022-12-07 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location_tracker_client', '0005_location_location_mode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='headers',
        ),
        migrations.AddField(
            model_name='device',
            name='manufacturer',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='device',
            name='owner_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='device',
            name='sku',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='city',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='country',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='state',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
