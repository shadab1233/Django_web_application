# Generated by Django 5.0.1 on 2024-01-12 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='students',
            old_name='phone',
            new_name='roll',
        ),
    ]
