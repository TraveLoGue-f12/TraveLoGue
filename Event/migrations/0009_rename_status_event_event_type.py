# Generated by Django 4.1 on 2022-10-30 23:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0008_event_status_event'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='status_event',
            new_name='type',
        ),
    ]