# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seedbank', '0003_auto_20141206_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commonname',
            name='language',
            field=models.CharField(default=b'English', max_length=45, choices=[(b'english', b'English'), (b'thai', b'Thai')]),
            preserve_default=True,
        ),
    ]
