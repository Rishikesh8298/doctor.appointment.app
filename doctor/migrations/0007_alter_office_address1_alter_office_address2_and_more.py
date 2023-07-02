# Generated by Django 4.1 on 2023-06-29 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0006_rename_zip_office_zipcode_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='office',
            name='address1',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='office',
            name='address2',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='office',
            name='city',
            field=models.CharField(default=None, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='office',
            name='country',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='office',
            name='first_consultation_fee',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='office',
            name='followup_consultation_fee',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='office',
            name='office_name',
            field=models.CharField(default=None, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='office',
            name='state',
            field=models.CharField(default=None, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='office',
            name='time_slot_per_patient_time',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='office',
            name='zipcode',
            field=models.CharField(default=None, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='officedoctoravailability',
            name='day_of_week',
            field=models.CharField(default=None, max_length=15),
        ),
        migrations.AlterField(
            model_name='officedoctoravailability',
            name='end_time',
            field=models.TimeField(default=None),
        ),
        migrations.AlterField(
            model_name='officedoctoravailability',
            name='start_time',
            field=models.TimeField(default=None),
        ),
        migrations.AlterField(
            model_name='qualification',
            name='institute_name',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='qualification',
            name='name',
            field=models.CharField(db_column='qualification_name', default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='qualification',
            name='passing_year',
            field=models.DateField(default=None, null=True),
        ),
    ]
