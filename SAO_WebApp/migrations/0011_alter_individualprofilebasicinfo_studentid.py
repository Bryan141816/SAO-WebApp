# Generated by Django 5.0.4 on 2024-05-21 12:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SAO_WebApp', '0010_alter_individualprofilebasicinfo_studentid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individualprofilebasicinfo',
            name='studentId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SAO_WebApp.studentinfo'),
        ),
    ]
