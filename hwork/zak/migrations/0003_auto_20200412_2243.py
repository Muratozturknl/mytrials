# Generated by Django 3.0.4 on 2020-04-12 22:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zak', '0002_auto_20200412_2237'),
    ]

    operations = [
        migrations.RenameField(
            model_name='zak',
            old_name='title',
            new_name='task',
        ),
    ]
