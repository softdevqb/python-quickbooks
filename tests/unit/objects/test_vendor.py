import unittest

from quickbooks.objects.vendor import Vendor


class VendorTests(unittest.TestCase):
    def test_unicode(self):
        vendor = Vendor()
        vendor.DisplayName = "test"

        self.assertEquals(vendor.__unicode__(), "test")

    def test_to_ref(self):
        vendor = Vendor()
        vendor.DisplayName = "test"
        vendor.Id = 100

        ref = vendor.to_ref()

        self.assertEquals(ref.name, "test")
        self.assertEquals(ref.type, "Vendor")
        self.assertEquals(ref.value, 100)
