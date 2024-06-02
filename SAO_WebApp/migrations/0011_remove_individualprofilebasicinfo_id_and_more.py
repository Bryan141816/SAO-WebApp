# Generated by Django 5.0.4 on 2024-06-02 08:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SAO_WebApp', '0010_alter_individualprofilebasicinfo_typeofscholarship'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='individualprofilebasicinfo',
            name='id',
        ),
        migrations.AlterField(
            model_name='individualprofilebasicinfo',
            name='studentId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='SAO_WebApp.studentinfo'),
        ),
    ]
