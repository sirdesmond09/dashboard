# Generated by Django 2.2.6 on 2019-11-29 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dboard', '0002_auto_20191129_1037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lawyers',
            name='confirm_password',
        ),
    ]
