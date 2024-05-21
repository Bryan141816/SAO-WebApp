# Generated by Django 5.0.4 on 2024-05-21 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SAO_WebApp', '0007_alter_counseling_schedule_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counseling_schedule',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Declined', 'Declined'), ('Pending', 'Pending'), ('Expired', 'Expired')], default='Pending', max_length=10),
        ),
    ]