import os
import unittest

from quickbooks.objects.customer import Customer
from quickbooks.objects.item import Item
from quickbooks.client import QuickBooks
from quickbooks.objects.creditmemo import CreditMemo, CreditMemoLine, SalesItemLineDetail


class CreditMemoTest(unittest.TestCase):
    def setUp(self):
        QuickBooks(
            sandbox=True,
            consumer_key=os.environ.get('CONSUMER_KEY'),
            consumer_secret=os.environ.get('CONSUMER_SECRET'),
            access_token=os.environ.get('ACCESS_TOKEN'),
            access_token_secret=os.environ.get('ACCESS_TOKEN_SECRET'),
            company_id=os.environ.get('COMPANY_ID')
        )

    def test_create(self):
        customer = Customer.all(max_results=1)[0]
        item = Item.all(max_results=1)[0]

        credit_memo = CreditMemo()
        credit_memo.CustomerRef = customer.to_ref()

        detail_line = CreditMemoLine()
        detail_line.LineNum = "1"
        detail_line.Description = "Test Description"
        detail_line.Amount = 100
        detail_line.DetailType = "SalesItemLineDetail"
        detail_line.SalesItemLineDetail = SalesItemLineDetail()
        detail_line.SalesItemLineDetail.ItemRef = item.to_ref()
        credit_memo.Line.append(detail_line)
        credit_memo.save()

        query_credit_memo = CreditMemo.get(credit_memo.Id)

        self.assertEquals(credit_memo.Id, query_credit_memo.Id)
        self.assertEquals(query_credit_memo.CustomerRef.value, customer.Id)
        self.assertEquals(len(query_credit_memo.Line), 1)
