# Generated by Django 4.1.7 on 2023-03-22 03:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userincident', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='incident',
            old_name='user',
            new_name='user_id',
        ),
    ]
