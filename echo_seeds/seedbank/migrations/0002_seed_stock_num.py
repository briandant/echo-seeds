# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seedbank', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='seed',
            name='stock_num',
            field=models.IntegerField(max_length=5, unique=True, null=True),
            preserve_default=True,
        ),
    ]
