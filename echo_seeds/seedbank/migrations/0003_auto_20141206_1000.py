# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seedbank', '0002_seed_stock_num'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commonname',
            old_name='common_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='family',
            old_name='family',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='germination',
            old_name='germ_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='germination',
            old_name='germ_method',
            new_name='method',
        ),
        migrations.RenameField(
            model_name='germination',
            old_name='germ_rate',
            new_name='rate',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='location_code',
            new_name='code',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='location_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='location_type',
            new_name='type',
        ),
        migrations.RenameField(
            model_name='scientificname',
            old_name='scientific_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='supplier',
            old_name='supplier_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='suppliertype',
            old_name='supplier_type',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='variety',
            old_name='variety',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='seed',
            name='germination',
        ),
        migrations.AddField(
            model_name='germination',
            name='seed',
            field=models.ForeignKey(to='seedbank.Seed', null=True),
            preserve_default=True,
        ),
    ]
