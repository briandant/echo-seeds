"""
Scripts for importing data into the system.  More information about where
this data comes from and lives can be found in the docs on Migrating Data From
Old Systems.
"""

__author__ = 'briandant'

import csv
from os.path import join
from django.conf import settings
from django.db import IntegrityError
from seedbank.models import (
    CommonName, Family, Location,
    ScientificName, Seed, Variety
)

FIELD_MAPPING = (
    ('Stock Item',            '_set_stock_item'),
    ('Scientific Name',       '_set_scientific_name'),
    ('Blank',                 None),
    ('Accession',             '_set_accession'),
    ('Lot',                   '_set_lot'),
    ('Combined',              None),
    ('Blank',                 None),
    ('Common Name - English', '_set_english_common_name'),
    ('Common Name - Thai',    '_set_thai_common_name'),
    ('Variety',               '_set_variety'),
    ('Current Germ Date',     None),
    ('Current Germ Rate',     None),
    ('Default Location Code', '_set_default_location_code'),
    ('Default Location Name', '_set_default_location_name'),
    ('Family Name',           '_set_default_family_name'),
    ('Planting Instructions', '_set_planting_instructions'),
    ('Cost of Goods',         '_set_cost_of_goods'),
)

BASE_DIR = settings.BASE_DIR
DATA_DIR = join(BASE_DIR, 'data')
SEED_DATA_FILE = join(DATA_DIR, 'initial-seed-data.csv')


class SeedWriter(object):

    def __init__(self, row):

        self.row = row
        self.seed = Seed()

    def write(self):

        for i, data in enumerate(self.row):
            field = FIELD_MAPPING[i][0]
            action = FIELD_MAPPING[i][1]
            print ">>> Field: %s" % field
            print ">>> Function: %s" % action
            print ">>> Data: %s" % data
            print "------------------------"

            if action:
                getattr(self, action)(data)

        objects = ['family', 'scientific_name', 'variety', 'common_name', 'seed']

        print "#############################################################"
        for o in objects:
            if hasattr(self, o):
                try:
                    getattr(self, o).save()
                except IntegrityError as e:
                    if 'Key (accession_num, lot_num)' not in e.message:
                        raise
                    else:
                        pass  # TODO: Log this.

    def _set_stock_item(self, data):

        self.seed.stock_num = data

    def _set_scientific_name(self, data):

        sci_name = ScientificName.objects.get_or_create(name=data.strip())[0]
        self.scientific_name = sci_name
        self.seed.scientific_name = sci_name

    def _set_accession(self, data):

        self.seed.accession_num = data.replace(' ', '')

    def _set_lot(self, data):

        self.seed.lot_num = data.replace(' ', '')

    def _set_english_common_name(self, data):

        if data:
            comm_name = CommonName.objects.get_or_create(
                name=data.strip(),
                scientific_name=self.scientific_name,
                language="english"
            )[0]
            self.common_name = comm_name
            self.seed.common_name = comm_name

    def _set_thai_common_name(self, data):

        if data:
            data = data.strip().decode('utf-8')
            comm_name = CommonName.objects.get_or_create(
                name=data,
                language="thai",
                scientific_name=self.scientific_name
            )[0]
            self.common_name = comm_name
            self.seed.common_name = comm_name

    def _set_variety(self, data):

        if data:
            variety = Variety.objects.get_or_create(
                name=data.strip(),
                scientific_name=self.scientific_name,
            )[0]
            self.variety = variety
            self.seed.variety = variety

    def _set_default_location_code(self, data):

        if data and data.replace(" ", ""):
            loc = Location.objects.get_or_create(code=data)[0]
            self.location = loc
            self.seed.acquisition_location = self.location

    def _set_default_location_name(self, data):

        if hasattr(self, 'location') and data and data.replace(" ", ""):
            self.location.name = data.strip()

    def _set_default_family_name(self, data):

        if data:
            fam = Family.objects.get_or_create(name=data.strip())[0]
            self.family = fam
            self.seed.family = fam

    def _set_planting_instructions(self, data):

        if hasattr(self, 'variety'):
            self.variety.planting_instructions = data

    def _set_cost_of_goods(self, data):

        if data:
            data = data.strip('$')
            data = float(data)
            self.seed.cost = data


def _delete_all():

    print ">>> Deleting all data."
    Seed.objects.all().delete()
    Variety.objects.all().delete()
    ScientificName.objects.all().delete()
    CommonName.objects.all().delete()
    Family.objects.all().delete()
    Location.objects.all().delete()
    print ">>> Database data cleared."


def write(delete=True):

    if delete:
        _delete_all()

    # Read the row
    # for item in row, either just write it or run the function that matcehds is
    with open(SEED_DATA_FILE, 'rt') as f:
        reader = csv.reader(f)
        for row in reader:
            writer = SeedWriter(row)
            writer.write()
