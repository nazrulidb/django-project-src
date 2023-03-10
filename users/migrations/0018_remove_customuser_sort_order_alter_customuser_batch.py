# Generated by Django 4.0.5 on 2022-07-21 00:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0010_alter_batch_degree'),
        ('users', '0017_alter_customuser_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='sort_order',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='batch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='students_batch', to='departments.batch'),
        ),
    ]
