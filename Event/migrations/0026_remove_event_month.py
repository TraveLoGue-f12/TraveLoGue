# Generated by Django 4.1 on 2022-12-04 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0025_remove_event_image_remove_event_imageurl'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='month',
        ),
    ]
