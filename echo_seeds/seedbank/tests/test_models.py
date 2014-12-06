from django.test import TestCase
from seedbank.models import Seed


class TestSeed(TestCase):

    def setUp(self):

        self.seed = Seed()

    def test_original_stock_number(self):
        """The original stock numbers were zero-leading. We converted those
        to ints, but have a method to get 'em back out as we originally got
        them."""

        original = "00040"
        self.seed.stock_num = int(original.lstrip('0'))

        self.assertEqual(self.seed.get_original_stock_num(), original)
