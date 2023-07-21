# Generated by Django 4.1 on 2023-07-09 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientinfo',
            name='firstname',
            field=models.CharField(db_column='first_name', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='patientinfo',
            name='gender',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='patientinfo',
            name='lastname',
            field=models.CharField(db_column='last_name', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='patientinfo',
            name='phone',
            field=models.CharField(max_length=15, null=True),
        ),
    ]