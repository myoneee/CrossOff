# Generated by Django 3.2 on 2021-07-26 05:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20210725_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthdate',
            field=models.DateField(default=datetime.datetime(2021, 7, 26, 5, 1, 48, 248707, tzinfo=utc)),
        ),
    ]
