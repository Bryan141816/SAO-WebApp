# Generated by Django 5.0.4 on 2024-05-18 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SAO_WebApp', '0008_remove_individualprofilebasicinfo_sexualorientationother'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestArray',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('myarray', models.JSONField()),
            ],
        ),
    ]
