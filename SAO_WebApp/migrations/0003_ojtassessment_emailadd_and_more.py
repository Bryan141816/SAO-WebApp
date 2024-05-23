# Generated by Django 5.0.4 on 2024-05-23 13:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SAO_WebApp', '0002_ojtassessment_dateaccepted'),
    ]

    operations = [
        migrations.AddField(
            model_name='ojtassessment',
            name='emailadd',
            field=models.EmailField(default='2024-24-04', max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ojtassessment',
            name='dateAccepted',
            field=models.DateField(default=datetime.datetime(2024, 5, 23, 13, 48, 1, 661448, tzinfo=datetime.timezone.utc)),
        ),
    ]
