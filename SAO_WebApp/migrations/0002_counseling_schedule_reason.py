# Generated by Django 5.0.4 on 2024-05-05 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SAO_WebApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='counseling_schedule',
            name='reason',
            field=models.CharField(default='no reason', max_length=255),
            preserve_default=False,
        ),
    ]