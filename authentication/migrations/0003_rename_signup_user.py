# Generated by Django 4.1.2 on 2023-01-31 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('authentication', '0002_signup_delete_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='signup',
            new_name='User',
        ),
    ]
