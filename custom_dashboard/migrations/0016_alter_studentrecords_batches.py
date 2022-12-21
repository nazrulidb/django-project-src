# Generated by Django 4.0.5 on 2022-09-18 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0017_alter_batchyear_unique_together_batchyear_level_and_more'),
        ('custom_dashboard', '0015_alter_studentrecords_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentrecords',
            name='batches',
            field=models.ManyToManyField(related_name='student_record_year_batch', to='departments.batchyear', verbose_name='Batches'),
        ),
    ]