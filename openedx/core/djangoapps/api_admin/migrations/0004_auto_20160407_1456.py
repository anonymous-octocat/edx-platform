# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_admin', '0003_auto_20160404_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='apiaccessrequest',
            name='base_url',
            field=models.CharField(default=b'', max_length=255),
        ),
        migrations.AddField(
            model_name='apiaccessrequest',
            name='contacted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='historicalapiaccessrequest',
            name='base_url',
            field=models.CharField(default=b'', max_length=255),
        ),
        migrations.AddField(
            model_name='historicalapiaccessrequest',
            name='contacted',
            field=models.BooleanField(default=False),
        ),
    ]
