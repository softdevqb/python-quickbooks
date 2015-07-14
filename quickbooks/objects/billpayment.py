from base import QuickbooksBaseObject, Ref, LinkedTxn, QuickbooksManagedObject


class CheckPayment(QuickbooksBaseObject):
    class_dict = {
        "BankAccountRef": Ref
    }

    qbo_object_name = "CheckPayment"

    def __init__(self):
        super(CheckPayment, self).__init__()
        self.PrintStatus = ""
        self.BankAccountRef = None


class BillPaymentLine(QuickbooksBaseObject):
    list_dict = {
        "LinkedTxn": LinkedTxn
    }

    qbo_object_name = "Line"

    def __init__(self):
        super(BillPaymentLine, self).__init__()
        self.Amount = 0
        self.LinkedTxn = []

    def __unicode__(self):
        return self.Amount


class BillPayment(QuickbooksManagedObject):
    """
    QBO definition: A BillPayment entity represents the financial transaction of payment of bills that the
    business owner receives from a vendor for goods or services purchased from the vendor. QuickBooks Online
    supports bill payments through a credit card or a checking account.
    BillPayment.TotalAmt is the total amount associated with this payment. This includes the total of all the
    payments from the payment line details. If TotalAmt is greater than the total on the lines being paid,
    the overpayment is treated as a credit and exposed as such on the QuickBooks UI. The total amount
    cannot be negative.
    """

    class_dict = {
        "VendorRef": Ref,
        "CheckPayment": CheckPayment,
        "APAccountRef": Ref,
    }

    list_dict = {
        "Line": BillPaymentLine
    }

    qbo_object_name = "BillPayment"

    def __init__(self):
        super(BillPayment, self).__init__()
        self.PayType = ""
        self.TotalAmt = 0
        self.TxnDate = ""
        self.PrivateNote = ""

        self.VendorRef = None
        self.CheckPayment = None
        self.APAccountRef = None

        self.Line = []

