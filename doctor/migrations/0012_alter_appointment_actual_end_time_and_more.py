# Generated by Django 4.1 on 2023-07-09 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0011_alter_doctoravailability_day_of_week_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='actual_end_time',
            field=models.CharField(default='09:30', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='probable_start_time',
            field=models.CharField(default='09:30', max_length=10, null=True),
        ),
    ]