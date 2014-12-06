# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seedbank', '0004_auto_20141206_1014'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supplier',
            old_name='supplier_type',
            new_name='type',
        ),
        migrations.AlterField(
            model_name='location',
            name='code',
            field=models.CharField(max_length=45, choices=[(b'ECHO-US', 'ECHO-US'), (b'ECHO-THAI', 'ECHO-THAI')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(max_length=45, choices=[(b'FLORIDA', 'Florida'), (b'THAILAND', 'Thailand')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='location',
            name='type',
            field=models.CharField(max_length=45, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='seed',
            name='aquisition_date',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='seed',
            name='cost',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='seed',
            name='family',
            field=models.ForeignKey(to='seedbank.Family', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='seed',
            name='scientific_name',
            field=models.ForeignKey(to='seedbank.ScientificName', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='seed',
            name='supplier',
            field=models.ForeignKey(to='seedbank.Supplier', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='seed',
            name='variety',
            field=models.ForeignKey(to='seedbank.Variety', null=True),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='seed',
            unique_together=set([('accession_num', 'lot_num')]),
        ),
    ]
