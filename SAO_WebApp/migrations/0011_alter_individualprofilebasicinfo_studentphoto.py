# Generated by Django 5.0.4 on 2024-05-19 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SAO_WebApp', '0010_fileuploadtest_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individualprofilebasicinfo',
            name='studentPhoto',
            field=models.FileField(upload_to='studentPhoto'),
        ),
    ]