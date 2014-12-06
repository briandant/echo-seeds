# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommonName',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('common_name', models.CharField(max_length=45)),
                ('language', models.CharField(default=b'English', max_length=45, choices=[(b'English', b'English'), (b'Thai', b'Thai')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('family', models.CharField(max_length=45)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Germination',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('germ_rate', models.DecimalField(max_digits=2, decimal_places=2)),
                ('germ_date', models.DateField()),
                ('germ_method', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location_name', models.CharField(max_length=45)),
                ('location_code', models.CharField(max_length=45)),
                ('location_type', models.CharField(max_length=45)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ScientificName',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('scientific_name', models.CharField(max_length=45)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Seed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('accession_num', models.CharField(max_length=8)),
                ('lot_num', models.CharField(max_length=5)),
                ('aquisition_date', models.DateField()),
                ('cost', models.DecimalField(max_digits=6, decimal_places=2)),
                ('aquisition_location', models.ForeignKey(to='seedbank.Location')),
                ('family', models.ForeignKey(to='seedbank.Family')),
                ('germination', models.ForeignKey(to='seedbank.Germination')),
                ('scientific_name', models.ForeignKey(to='seedbank.ScientificName')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('supplier_name', models.CharField(max_length=45)),
                ('contact_first_name', models.CharField(max_length=45)),
                ('contact_last_name', models.CharField(max_length=45)),
                ('contact_phone', models.CharField(max_length=15)),
                ('contact_email', models.EmailField(max_length=75)),
                ('address_one', models.CharField(max_length=255)),
                ('address_two', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=45)),
                ('zip_code', models.IntegerField(max_length=10)),
                ('country', models.CharField(max_length=45)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=75)),
                ('website', models.URLField()),
                ('primary_seed_bank', models.ForeignKey(to='seedbank.Location')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SupplierType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('supplier_type', models.CharField(max_length=45)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Variety',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('variety', models.CharField(max_length=45)),
                ('seed_color', models.CharField(max_length=75)),
                ('parts_to_harvest', models.TextField()),
                ('unique_characteristics', models.TextField()),
                ('planting_intructions', models.TextField()),
                ('scientific_name', models.ForeignKey(to='seedbank.ScientificName')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='supplier',
            name='supplier_type',
            field=models.ForeignKey(to='seedbank.SupplierType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='seed',
            name='supplier',
            field=models.ForeignKey(to='seedbank.Supplier'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='seed',
            name='variety',
            field=models.ForeignKey(to='seedbank.Variety'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='commonname',
            name='scientific_name',
            field=models.ForeignKey(to='seedbank.ScientificName'),
            preserve_default=True,
        ),
    ]
