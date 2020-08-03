# Generated by Django 3.0.8 on 2020-08-02 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200802_1147'),
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.ForumUser'),
        ),
        migrations.AlterField(
            model_name='thread',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.ForumUser'),
        ),
        migrations.AlterField(
            model_name='userthreadevent',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='user.ForumUser'),
        ),
    ]
