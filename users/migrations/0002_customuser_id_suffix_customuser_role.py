# Generated by Django 4.0.5 on 2022-06-24 08:07

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='id_suffix',
            field=models.CharField(max_length=3, null=True, validators=[django.core.validators.RegexValidator(message='Numbers only', regex='^[0-9]+$')]),
        ),
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_role', to='auth.group', verbose_name='Role'),
        ),
    ]
