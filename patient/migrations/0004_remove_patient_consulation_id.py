# Generated by Django 4.1.2 on 2023-02-01 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0003_alter_patient_consulation_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='Consulation_ID',
        ),
    ]