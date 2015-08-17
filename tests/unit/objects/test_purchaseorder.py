import unittest

from quickbooks.objects.purchaseorder import PurchaseOrderLine, PurchaseOrder


class PurchaseOrderLineTests(unittest.TestCase):
    def test_unicode(self):
        purchase_line = PurchaseOrderLine()
        purchase_line.Amount = 100

        self.assertEquals(purchase_line.__unicode__(), 100)


class PurchaseOrderTests(unittest.TestCase):
    def test_unicode(self):
        purchase_order = PurchaseOrder()
        purchase_order.TotalAmt = 1000

        self.assertEquals(purchase_order.__unicode__(), 1000)