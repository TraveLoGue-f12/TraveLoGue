# Generated by Django 4.1 on 2022-11-01 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0009_question_title_alter_answer_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
