# Generated by Django 4.0.5 on 2022-07-15 23:47

from django.db import migrations, models
import django.db.models.deletion
import wagtail.contrib.routable_page.models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0069_log_entry_jsonfield'),
        ('institutes', '0005_customdocument_data'),
        ('students', '0004_alter_studenthomepage_announcement'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentHomepageRoute',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail.contrib.routable_page.models.RoutablePageMixin, 'wagtailcore.page'),
        ),
        migrations.AlterField(
            model_name='studenthomepage',
            name='institute',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_homepage', to='institutes.institute'),
        ),
    ]