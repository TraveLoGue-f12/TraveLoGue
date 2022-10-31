# Generated by Django 4.1 on 2022-10-27 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ObjekWisata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('title', models.CharField(max_length=25)),
                ('deskripsi', models.CharField(max_length=50)),
                ('alamat', models.URLField()),
            ],
        ),
    ]