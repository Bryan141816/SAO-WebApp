# Generated by Django 5.0.4 on 2024-05-18 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SAO_WebApp', '0006_individualprofilebasicinfo_sexualorientationother_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='individualprofilebasicinfo',
            name='fatherCTU',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='individualprofilebasicinfo',
            name='motherCTU',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
