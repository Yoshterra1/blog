# Generated by Django 2.2.3 on 2019-07-11 14:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0009_auto_20190711_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmessage',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 11, 14, 55, 39, 199561, tzinfo=utc)),
        ),
    ]
