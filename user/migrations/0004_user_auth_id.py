# Generated by Django 4.1.2 on 2023-01-31 21:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0003_remove_user_city_remove_user_phone_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='auth_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]