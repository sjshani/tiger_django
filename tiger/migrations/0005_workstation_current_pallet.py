# Generated by Django 5.1.1 on 2024-10-15 08:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiger', '0004_remove_workstation_battery_test_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='workstation',
            name='current_pallet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tiger.incomingpallet'),
        ),
    ]
