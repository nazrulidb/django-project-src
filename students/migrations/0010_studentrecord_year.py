# Generated by Django 4.0.8 on 2022-11-03 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0009_studentrecord_has_retake'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentrecord',
            name='year',
            field=models.IntegerField(null=True),
        ),
    ]
