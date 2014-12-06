# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seedbank', '0005_auto_20141206_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seed',
            name='stock_num',
            field=models.CharField(max_length=5, null=True),
            preserve_default=True,
        ),
    ]
