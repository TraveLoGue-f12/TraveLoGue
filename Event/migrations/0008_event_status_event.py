# Generated by Django 4.1 on 2022-10-30 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0007_event_imageurl'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='status_event',
            field=models.CharField(choices=[('Music', 'Music'), ('Culinary', 'Culinary'), ('Sport', 'Sport'), ('Indonesia Culture', 'Indonesia Culture'), ('Local Festival', 'Local Festival'), ('Others', 'Others')], default='', max_length=20),
        ),
    ]
