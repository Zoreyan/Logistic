# Generated by Django 4.1.7 on 2023-03-27 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_driver_license'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='status',
            field=models.BooleanField(default=False, null=True, verbose_name='На рейсе'),
        ),
    ]