# Generated by Django 4.1.1 on 2022-11-29 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_remove_page_javascript_remove_page_style_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='meta',
        ),
        migrations.AddField(
            model_name='meta',
            name='page',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.page'),
        ),
    ]