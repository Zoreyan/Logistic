# Generated by Django 4.1.7 on 2023-03-28 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_rename_company_shipment_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipment',
            name='phone_number',
            field=models.CharField(max_length=15, null=True, verbose_name='Контактный номер'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Описание'),
        ),
    ]
