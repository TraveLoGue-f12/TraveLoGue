# Generated by Django 4.1 on 2022-11-01 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0023_alter_event_description_alter_event_place_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(max_length=700),
        ),
        migrations.AlterField(
            model_name='event',
            name='place',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
