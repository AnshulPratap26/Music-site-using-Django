# Generated by Django 2.2.4 on 2019-10-25 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='music',
            name='audio_file',
        ),
    ]