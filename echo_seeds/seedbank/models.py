from django.db import models
from django.utils.translation import ugettext_lazy as _


LOCATIONS = {
    'names': (
        ('FLORIDA', _('Florida'),),
        ('THAILAND', _('Thailand'),)
    ),
    'codes': (
        ('ECHO-US', _('ECHO-US'),),
        ('ECHO-THAI', _('ECHO-THAI'),),
        ('ECHO-ASIA  MASTER', _('ECHO-ASIA MASTER'),)
    ),
}


class Location(models.Model):
    """
    The seedbank. The system supports multiple seedbanks, so each one can
    have it's own location.
    """

    name = models.CharField(max_length=45, blank=False, choices=LOCATIONS['names'])
    code = models.CharField(max_length=45, blank=False, choices=LOCATIONS['codes'])
    type = models.CharField(max_length=45, null=True, blank=True)

    def __unicode__(self):
        return self.name


class Family(models.Model):
    """
    TODO: Description of class
    """
    name = models.CharField(max_length=45, blank=False)

    def __unicode__(self):
        return self.name


class ScientificName(models.Model):
    """
    TODO: Description of class
    """
    name = models.CharField(max_length=45, blank=False)

    def __unicode__(self):
        return self.name

    class Meta:

        ordering = ('name',)


class Variety(models.Model):
    """
    TODO: Description of class
    """
    name = models.CharField(max_length=45, blank=False)
    seed_color = models.CharField(max_length=75, null=True)
    parts_to_harvest = models.TextField(null=True)
    unique_characteristics = models.TextField(null=True)
    planting_intructions = models.TextField(null=True)

    scientific_name = models.ForeignKey('ScientificName')

    def __unicode__(self):
        return self.name

    class Meta:

        ordering = ('name',)


class Germination(models.Model):
    """
    TODO: Description of class
    """
    rate = models.DecimalField(decimal_places=2, max_digits=2, blank=False)
    date = models.DateField(blank=False)
    method = models.TextField()
    seed = models.ForeignKey('Seed', null=True)  # TODO: Make non-nullable.

    def __unicode__(self):
        return self.rate


class CommonName(models.Model):
    """
    TODO: Description of class
    """
    name = models.CharField(max_length=45)
    langs = (("english", "English"), ("thai", "Thai"))
    language = models.CharField(max_length=45, choices=langs, default="english")
    scientific_name = models.ForeignKey('ScientificName')

    def __unicode__(self):
        return self.name

    class Meta:

        ordering = ('language', 'name',)


class SupplierType(models.Model):
    """
    TODO: Description of class
    """
    name = models.CharField(max_length=45)

    def __unicode__(self):
        return self.name

    class Meta:

        ordering = ('name',)


class Supplier(models.Model):
    """
    TODO: Description of class
    """
    name = models.CharField(max_length=45, blank=False)
    contact_first_name = models.CharField(max_length=45)
    contact_last_name = models.CharField(max_length=45)
    contact_phone = models.CharField(max_length=15)
    contact_email = models.EmailField()
    address_one = models.CharField(max_length=255, blank=False)
    address_two = models.CharField(max_length=255)
    city = models.CharField(max_length=255, blank=False)
    state = models.CharField(max_length=45)
    zip_code = models.IntegerField(max_length=10)
    country = models.CharField(max_length=45, blank=False)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    website = models.URLField()

    type = models.ForeignKey(SupplierType)
    primary_seed_bank = models.ForeignKey(Location)

    def __unicode__(self):
        return self.supplier_name

    class Meta:

        ordering = ('name',)


class Seed(models.Model):
    """
    TODO: Description of class
    """

    accession_num = models.CharField(max_length=8, blank=False)
    acquisition_date = models.DateField(null=True)
    acquisition_location = models.ForeignKey('Location', null=True)
    common_name = models.ForeignKey('CommonName', null=True)
    cost = models.DecimalField(decimal_places=2, max_digits=6, null=True)
    family = models.ForeignKey('Family', null=True)
    lot_num = models.CharField(max_length=5, blank=False)
    scientific_name = models.ForeignKey('ScientificName', null=True)
    supplier = models.ForeignKey('Supplier', null=True)
    stock_num = models.CharField(max_length=5, null=True)
    variety = models.ForeignKey('Variety', null=True)

    class Meta:
        unique_together = ('accession_num', 'lot_num',)
        ordering = ('accession_num', 'lot_num')

    def __unicode__(self):
        return "{}-{}".format(self.accession_num, self.lot_num)
