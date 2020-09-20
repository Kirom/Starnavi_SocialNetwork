# Generated by Django 3.1.1 on 2020-09-20 13:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20200920_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='like_date',
            field=models.DateField(default=datetime.datetime(2020, 9, 20, 13, 21, 31, 387781, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='creation_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
