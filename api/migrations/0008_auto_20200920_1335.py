# Generated by Django 3.1.1 on 2020-09-20 13:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20200920_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='like_date',
            field=models.DateField(default=datetime.datetime(2020, 9, 20, 13, 35, 1, 130810, tzinfo=utc)),
        ),
    ]