# Generated by Django 4.0.5 on 2022-07-11 04:52

from django.db import migrations
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0010_alter_batch_degree'),
        ('users', '0014_alter_customuser_managers_delete_studentprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='batch',
            field=modelcluster.fields.ParentalKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='students_batch', to='departments.batch'),
        ),
    ]