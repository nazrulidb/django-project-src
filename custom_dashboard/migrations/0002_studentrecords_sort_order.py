# Generated by Django 4.0.5 on 2022-07-03 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentrecords',
            name='sort_order',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
    ]
