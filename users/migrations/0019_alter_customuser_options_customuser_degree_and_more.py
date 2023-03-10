# Generated by Django 4.0.5 on 2022-08-31 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('institutes', '0007_alter_institute_unique_together_customdocument_batch_and_more'),
        ('departments', '0013_alter_batch_unique_together_batch_collection_key_and_more'),
        ('users', '0018_remove_customuser_sort_order_alter_customuser_batch'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
        migrations.AddField(
            model_name='customuser',
            name='degree',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_degree', to='institutes.degree'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='batch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='students_batch', to='departments.batchyear'),
        ),
    ]
