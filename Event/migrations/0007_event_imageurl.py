# Generated by Django 4.1 on 2022-10-30 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0006_alter_event_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='imageURL',
            field=models.TextField(null=True),
        ),
    ]