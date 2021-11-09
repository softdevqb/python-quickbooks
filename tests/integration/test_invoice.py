from quickbooks.objects.base import CustomerMemo
from quickbooks.objects.customer import Customer
from quickbooks.objects.detailline import SalesItemLine, SalesItemLineDetail
from quickbooks.objects.invoice import Invoice
from quickbooks.objects.item import Item
from tests.integration.test_base import QuickbooksTestCase
import uuid

class InvoiceTest(QuickbooksTestCase):

    def create_invoice(self, request_id=None):
        invoice = Invoice()

        line = SalesItemLine()
        line.LineNum = 1
        line.Description = "description"
        line.Amount = 100
        line.SalesItemLineDetail = SalesItemLineDetail()
        item = Item.all(max_results=1, qb=self.qb_client)[0]

        line.SalesItemLineDetail.ItemRef = item.to_ref()
        invoice.Line.append(line)

        customer = Customer.all(max_results=1, qb=self.qb_client)[0]
        invoice.CustomerRef = customer.to_ref()

        invoice.CustomerMemo = CustomerMemo()
        invoice.CustomerMemo.value = "Customer Memo"
        invoice.save(qb=self.qb_client, request_id=request_id)

    def test_create(self):
        invoice = self.create_invoice()
        query_invoice = Invoice.get(invoice.Id, qb=self.qb_client)

        self.assertEquals(query_invoice.CustomerRef.name, customer.DisplayName)
        self.assertEquals(query_invoice.CustomerMemo.value, "Customer Memo")
        self.assertEquals(query_invoice.Line[0].Description, "description")
        self.assertEquals(query_invoice.Line[0].Amount, 100.0)
    
    def test_create_idempotence(self):
        sample_request_id = str(uuid.uuid4())
        invoice = self.create_invoice(request_id=sample_request_id)
        duplicate_invoice = self.create_invoice(request_id=sample_request_id)

        # Assert that both returned invoices have the same id
        self.assertEquals(invoice.Id, duplicate_invoice.Id)

    def test_delete(self):
        # First create an invoice
        invoice = self.create_invoice()

        # Then delete
        invoice_id = invoice.Id
        invoice.delete(qb=self.qb_client)

        query_invoice = Invoice.filter(Id=invoice_id, qb=self.qb_client)
        self.assertEqual([], query_invoice)
