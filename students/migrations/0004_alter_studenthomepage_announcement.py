# Generated by Django 4.0.5 on 2022-07-13 00:57

from django.db import migrations
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_alter_studenthomepage_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studenthomepage',
            name='announcement',
            field=wagtail.fields.RichTextField(blank=True, null=True),
        ),
    ]
