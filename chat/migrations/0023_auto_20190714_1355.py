# Generated by Django 2.2.3 on 2019-07-14 13:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0022_auto_20190714_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmessage',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 14, 13, 55, 50, 460505, tzinfo=utc)),
        ),
    ]
