# Generated by Django 2.2.9 on 2019-12-19 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GhostProject', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]
