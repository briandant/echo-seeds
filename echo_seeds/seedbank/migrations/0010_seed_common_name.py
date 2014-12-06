# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seedbank', '0009_auto_20141206_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='seed',
            name='common_name',
            field=models.ForeignKey(to='seedbank.CommonName', null=True),
            preserve_default=True,
        ),
    ]
