# Generated by Django 4.0.8 on 2022-12-11 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_dashboard', '0028_alter_batchuploadresult_batch_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentrecords',
            name='level',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], default=1),
        ),
    ]
