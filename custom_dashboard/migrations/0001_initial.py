# Generated by Django 4.0.5 on 2022-07-03 18:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtaildocs', '0012_uploadeddocument'),
        ('institutes', '0002_degree'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentRecords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('decline', 'Decline'), ('approve', 'Approve')], default='pending', max_length=50)),
                ('assigned_controller', models.ForeignKey(blank=True, limit_choices_to={'role__name': 'Controller of Exam'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_controller', to=settings.AUTH_USER_MODEL)),
                ('assigned_pr', models.ForeignKey(blank=True, limit_choices_to={'role__name': 'Proof Reader of Exam'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_proof_reader', to=settings.AUTH_USER_MODEL)),
                ('institute', modelcluster.fields.ParentalKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='institute_dashboard', to='institutes.institute')),
                ('link_document', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtaildocs.document')),
            ],
        ),
    ]
