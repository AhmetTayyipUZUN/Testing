# Generated by Django 2.2.2 on 2020-03-01 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='text',
            new_name='answer',
        ),
        migrations.AlterModelTable(
            name='answer',
            table='t_answer',
        ),
        migrations.AlterModelTable(
            name='question',
            table='t_question',
        ),
    ]
