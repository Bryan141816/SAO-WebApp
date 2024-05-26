# Generated by Django 5.0.4 on 2024-05-26 12:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SAO_WebApp', '0003_ojtassessment_emailadd_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='exit_interview_db',
            name='majorEvent',
            field=models.CharField(default='Test', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='exit_interview_db',
            name='exitinterviewId',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ojtassessment',
            name='dateAccepted',
            field=models.DateField(default=datetime.datetime(2024, 5, 26, 12, 8, 44, 941126, tzinfo=datetime.timezone.utc)),
        ),
    ]
