# Generated by Django 4.1 on 2022-10-31 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0007_alter_question_question_alter_question_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='title',
        ),
    ]
