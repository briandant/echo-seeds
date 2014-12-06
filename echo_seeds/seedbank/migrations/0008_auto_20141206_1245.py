# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seedbank', '0007_auto_20141206_1240'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seed',
            old_name='aquisition_date',
            new_name='acquisition_date',
        ),
        migrations.RenameField(
            model_name='seed',
            old_name='aquisition_location',
            new_name='acquisition_location',
        ),
    ]
