# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seedbank', '0006_auto_20141206_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commonname',
            name='language',
            field=models.CharField(default=b'english', max_length=45, choices=[(b'english', b'English'), (b'thai', b'Thai')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='variety',
            name='parts_to_harvest',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='variety',
            name='planting_intructions',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='variety',
            name='seed_color',
            field=models.CharField(max_length=75, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='variety',
            name='unique_characteristics',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
    ]
