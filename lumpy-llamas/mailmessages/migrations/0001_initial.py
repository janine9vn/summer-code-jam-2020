# Generated by Django 3.0.8 on 2020-08-09 09:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivateMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=3000)),
                ('subject', models.CharField(max_length=120)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('from_user',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL,
                                   to_field='username')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_user',
                                              to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
        ),
    ]