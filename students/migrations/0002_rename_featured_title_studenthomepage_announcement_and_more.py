# Generated by Django 4.0.5 on 2022-07-13 00:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studenthomepage',
            old_name='featured_title',
            new_name='announcement',
        ),
        migrations.RenameField(
            model_name='studenthomepage',
            old_name='feedback_background',
            new_name='logo',
        ),
        migrations.RemoveField(
            model_name='studenthomepage',
            name='short_intro',
        ),
    ]
