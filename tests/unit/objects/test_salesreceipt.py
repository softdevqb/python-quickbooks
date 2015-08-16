import unittest

from quickbooks.objects.salesreceipt import SalesItemLineDetail, SalesReceiptLine, SalesReceipt


class SalesReceiptLineTests(unittest.TestCase):
    def test_unicode(self):
        receipt_line = SalesReceiptLine()
        receipt_line.Amount = 100

        self.assertEquals(receipt_line.__unicode__(), 100)


class SalesItemLineDetailTests(unittest.TestCase):
    def test_unicode(self):
        item = SalesItemLineDetail()
        item.UnitPrice = 100

        self.assertEquals(item.__unicode__(), 100)


class SalesReceiptTests(unittest.TestCase):
    def test_unicode(self):
        sales_receipt = SalesReceipt()
        sales_receipt.TotalAmt = 100

        self.assertEquals(sales_receipt.__unicode__(), 100)