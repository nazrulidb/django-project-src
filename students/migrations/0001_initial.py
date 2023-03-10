# Generated by Django 4.0.5 on 2022-07-13 00:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0069_log_entry_jsonfield'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('institutes', '0005_customdocument_data'),
        ('wagtailimages', '0024_index_image_file_hash'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': 'Students',
            },
        ),
        migrations.CreateModel(
            name='StudentHomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('welcome_title', models.CharField(blank=True, max_length=500, null=True)),
                ('short_intro', models.CharField(blank=True, max_length=500, null=True)),
                ('featured_title', models.CharField(blank=True, max_length=500, null=True)),
                ('feedback_background', models.ForeignKey(blank=True, help_text='max size 1902x1100', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('institute', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student_homepage', to='institutes.institute')),
            ],
            options={
                'verbose_name': 'student_homepage',
            },
            bases=('wagtailcore.page',),
        ),
    ]
