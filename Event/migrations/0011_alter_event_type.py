# Generated by Django 4.1 on 2022-10-30 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0010_alter_event_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='type',
            field=models.CharField(choices=[('Music', 'Music'), ('Culinary', 'Culinary'), ('Sport', 'Sport'), ('Indonesia Culture', 'Indonesia Culture'), ('Local Festival', 'Local Festival'), ('Others', 'Others')], default='', max_length=20),
        ),
    ]
