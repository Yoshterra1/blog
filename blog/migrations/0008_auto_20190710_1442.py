# Generated by Django 2.2.3 on 2019-07-10 14:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190710_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 10, 14, 42, 51, 31681, tzinfo=utc)),
        ),
    ]
