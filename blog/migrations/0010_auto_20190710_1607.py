# Generated by Django 2.2.3 on 2019-07-10 16:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20190710_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 10, 16, 7, 25, 725382, tzinfo=utc)),
        ),
    ]
