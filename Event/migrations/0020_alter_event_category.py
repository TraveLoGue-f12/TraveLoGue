# Generated by Django 4.1 on 2022-10-31 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0019_rename_status_event_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
