# Generated by Django 4.1.4 on 2023-01-31 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
