# Generated by Django 5.0.6 on 2024-06-19 16:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_patient_patientrecords_patientid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientrecords',
            name='patientId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.patient'),
        ),
    ]
