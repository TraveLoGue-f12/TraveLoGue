# Generated by Django 4.1 on 2022-12-02 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('umkm', '0005_umkm_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='umkm',
            name='image',
        ),
        migrations.RemoveField(
            model_name='umkm',
            name='imageURL',
        ),
    ]
