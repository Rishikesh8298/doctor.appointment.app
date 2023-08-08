# Generated by Django 4.1 on 2023-07-28 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0014_appointment_reason_of_unavailability_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='reason_of_unavailability',
        ),
        migrations.CreateModel(
            name='Unavailability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_unavailability', models.DateField()),
                ('reason_of_unavailability', models.TextField(default='')),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.doctorinfo')),
            ],
        ),
    ]