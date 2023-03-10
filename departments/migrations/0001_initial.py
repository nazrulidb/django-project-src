# Generated by Django 4.0.5 on 2022-06-24 06:38

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('institutes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('name', models.CharField(max_length=120, null=True)),
                ('custom_id', models.CharField(blank=True, max_length=2, null=True, unique=True)),
                ('code', models.CharField(max_length=3, null=True, validators=[django.core.validators.RegexValidator(message='String only', regex='[a-zA-Z]')])),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('institute', modelcluster.fields.ParentalKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='departments', to='institutes.institute')),
            ],
            options={
                'verbose_name': 'Department',
                'verbose_name_plural': 'Departments',
                'get_latest_by': 'created_at',
                'unique_together': {('institute', 'name', 'code')},
            },
        ),
    ]
