# Generated by Django 3.0.4 on 2020-03-24 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('minizakgeld', '0003_auto_20200322_1656'),
    ]

    operations = [
        migrations.RenameField(
            model_name='zakgeld',
            old_name='person',
            new_name='child',
        ),
    ]