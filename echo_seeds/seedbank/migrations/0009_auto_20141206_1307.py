# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seedbank', '0008_auto_20141206_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seed',
            name='acquisition_location',
            field=models.ForeignKey(to='seedbank.Location', null=True),
            preserve_default=True,
        ),
    ]
