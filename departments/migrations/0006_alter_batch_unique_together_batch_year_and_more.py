# Generated by Django 4.0.5 on 2022-06-28 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0005_alter_batch_assigned_faculty_member_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='batch',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='batch',
            name='year',
            field=models.IntegerField(choices=[(2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022)], default=2022, verbose_name='year'),
        ),
        migrations.AlterUniqueTogether(
            name='batch',
            unique_together={('department', 'name', 'year')},
        ),
    ]
