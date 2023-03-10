# Generated by Django 4.0.5 on 2022-06-24 06:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('name', models.CharField(max_length=120, null=True)),
                ('custom_id', models.CharField(blank=True, max_length=2, null=True, unique=True)),
                ('code', models.CharField(max_length=3, null=True, validators=[django.core.validators.RegexValidator(message='String only', regex='[a-zA-Z]')])),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Institute',
                'verbose_name_plural': 'Institutes',
                'get_latest_by': 'created_at',
                'unique_together': {('name', 'code')},
            },
        ),
    ]
