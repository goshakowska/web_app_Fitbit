from django.test import SimpleTestCase
import client.discount_calculate as dc


class DiscountTest(SimpleTestCase):
    def test_calculate_price_after_discount_one_percent(self):
        self.assertEqual(dc.calcucate_price_after_discount(100, 1), 99)

    def test_calculate_price_after_discount_ten_percent(self):
        self.assertEqual(dc.calcucate_price_after_discount(100, 10), 90)

    def test_calculate_price_after_discount_fraction_with_tens_part(self):
        self.assertEqual(dc.calcucate_price_after_discount(10, 88), 1.2)

    def test_calculate_price_after_discount_fraction_with_hundredth_part(self):
        self.assertEqual(dc.calcucate_price_after_discount(99, 7), 92.07)

