# Generated by Django 4.0.5 on 2022-09-18 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('institutes', '0010_alter_institute_name'),
        ('custom_dashboard', '0020_studentrecords_year'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='studentrecords',
            unique_together={('institute', 'year', 'term', 'level')},
        ),
    ]
