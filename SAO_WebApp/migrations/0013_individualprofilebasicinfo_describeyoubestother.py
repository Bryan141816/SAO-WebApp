# Generated by Django 5.0.4 on 2024-05-19 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SAO_WebApp', '0012_alter_individualprofilebasicinfo_studentphoto'),
    ]

    operations = [
        migrations.AddField(
            model_name='individualprofilebasicinfo',
            name='describeYouBestOther',
            field=models.CharField(default=255, max_length=255),
        ),
    ]
