# Generated by Django 5.0.6 on 2024-06-19 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_pets_table_alter_users_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='phone_numer',
            new_name='phone_number',
        ),
    ]
