# Generated by Django 4.0.5 on 2022-07-21 00:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('institutes', '0005_customdocument_data'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('students', '0005_studenthomepageroute_alter_studenthomepage_institute'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studenthomepage',
            name='institute',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_homepage', to='institutes.institute'),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
