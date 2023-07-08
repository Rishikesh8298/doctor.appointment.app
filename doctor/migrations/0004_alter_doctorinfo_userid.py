# Generated by Django 4.1 on 2023-06-26 11:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('doctor', '0003_alter_doctorinfo_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorinfo',
            name='userid',
            field=models.ForeignKey(db_column='username', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]