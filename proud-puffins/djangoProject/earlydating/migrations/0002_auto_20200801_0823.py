# Generated by Django 3.0.8 on 2020-08-01 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('earlydating', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='Gender',
            new_name='gender',
        ),
    ]
