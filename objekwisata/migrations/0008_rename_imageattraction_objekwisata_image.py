# Generated by Django 4.1 on 2022-10-31 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('objekwisata', '0007_rename_image_objekwisata_imageattraction'),
    ]

    operations = [
        migrations.RenameField(
            model_name='objekwisata',
            old_name='imageAttraction',
            new_name='image',
        ),
    ]