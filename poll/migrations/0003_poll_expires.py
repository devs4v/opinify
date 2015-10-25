# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0002_remove_poll_expires'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='expires',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 25, 17, 52, 51, 968925, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
