# Generated by Django 4.1.7 on 2023-03-27 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_delivery_driver_remove_delivery_shipment_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='license_number',
        ),
        migrations.AddField(
            model_name='driver',
            name='license',
            field=models.ImageField(null=True, upload_to='licenses', verbose_name='Лицензии'),
        ),
    ]
