# Generated by Django 2.2.3 on 2019-07-11 14:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0008_auto_20190711_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmessage',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 11, 14, 52, 45, 199358, tzinfo=utc)),
        ),
    ]
