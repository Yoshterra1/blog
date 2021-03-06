# Generated by Django 2.2.3 on 2019-07-12 16:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20190712_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='post_id',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comments',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 12, 16, 21, 18, 415090, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 12, 16, 21, 18, 414654, tzinfo=utc)),
        ),
    ]
