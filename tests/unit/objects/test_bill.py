import unittest

from quickbooks import QuickBooks
from quickbooks.objects.bill import Bill, BillLine, AccountBasedExpenseLineDetail, ItemBasedExpenseLineDetail


class AccountBasedExpenseLineDetailTests(unittest.TestCase):
    def test_unicode(self):
        acct_detail = AccountBasedExpenseLineDetail()
        acct_detail.BillableStatus = "test"

        self.assertEquals(str(acct_detail), "test")


class BillTests(unittest.TestCase):
    def test_unicode(self):
        bill = Bill()
        bill.Balance = 1000

        self.assertEquals(str(bill), "1000")

    def test_to_LinkedTxn(self):
        bill = Bill()
        bill.Id = 10

        linked_txn = bill.to_linked_txn()

        self.assertEquals(linked_txn.TxnId, bill.Id)
        self.assertEquals(linked_txn.TxnType, "Bill")
        self.assertEquals(linked_txn.TxnLineId, 1)

    def test_valid_object_name(self):
        obj = Bill()
        client = QuickBooks()
        result = client.isvalid_object_name(obj.qbo_object_name)

        self.assertTrue(result)

    def test_to_ref(self):
        bill = Bill()
        bill.DisplayName = "test"
        bill.Id = 100

        ref = bill.to_ref()

        self.assertEquals(ref.name, "test")
        self.assertEquals(ref.type, "Bill")
        self.assertEquals(ref.value, 100)


class BillLineTests(unittest.TestCase):
    def test_unicode(self):
        bill_line = BillLine()
        bill_line.Amount = 1000

        self.assertEquals(str(bill_line), "1000")


class ItemBasedExpenseLineDetailTest(unittest.TestCase):
    def test_init(self):
        detail = ItemBasedExpenseLineDetail()

        self.assertEquals(detail.BillableStatus, "")
        self.assertEquals(detail.UnitPrice, 0)
        self.assertEquals(detail.TaxInclusiveAmt, 0)
        self.assertEquals(detail.Qty, 0)
        self.assertEquals(detail.ItemRef, None)
        self.assertEquals(detail.ClassRef, None)
        self.assertEquals(detail.PriceLevelRef, None)
        self.assertEquals(detail.TaxCodeRef, None)
        self.assertEquals(detail.MarkupInfo, None)
        self.assertEquals(detail.CustomerRef, None)
