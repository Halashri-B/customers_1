# Generated by Django 4.2.3 on 2023-08-23 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers_1app', '0004_remove_record_area_pin_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='Pin',
            field=models.PositiveBigIntegerField(max_length=20),
        ),
    ]
