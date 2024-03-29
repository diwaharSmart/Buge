# Generated by Django 4.1.1 on 2023-03-15 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_datafield_datamodel_fieldparameters_modelfield_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fieldparameters',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fieldparameters',
            name='parapeter_group',
            field=models.CharField(blank=True, choices=[('Common Field Parameters', 'Common Field Parameters'), ('Text Fields', 'Text Fields'), ('Numeric Fields', 'Numeric Fields'), ('Date/Time Fields', 'Date/Time Fields'), ('Relationship Fields', 'Relationship Fields'), ('File/Image Fields', 'File/Image Fields'), ('Miscellaneous Fields', 'Miscellaneous Fields')], max_length=255, null=True),
        ),
    ]
