# Generated by Django 4.1.4 on 2023-01-28 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('University', models.CharField(max_length=200)),
                ('Specialization', models.CharField(max_length=200)),
                ('Detection_Price', models.IntegerField()),
                ('Resume', models.CharField(max_length=256)),
                ('User_ID', models.IntegerField()),
                ('Reservation_ID', models.IntegerField()),
                ('Consulation_ID', models.IntegerField()),
            ],
        ),
    ]
