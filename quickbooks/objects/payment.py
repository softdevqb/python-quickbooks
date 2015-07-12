from base import QuickbooksBaseObject, Ref, LinkedTxn


class PaymentLine(QuickbooksBaseObject):
    class_dict = {
        "LinkedTxn": LinkedTxn,
    }

    list_dict = {}

    def __init__(self):
        self.Amount = 0


class Payment(QuickbooksBaseObject):
    """
    QBO definition: A Payment entity records a payment in QuickBooks. The payment can be applied for a particular
    customer against multiple Invoices and Credit Memos. It can also be created without any Invoice or Credit Memo,
    by just specifying an amount.

        - A Payment can be updated as a full update or a sparse update.
        - A Payment can be linked to multiple Invoices and Credit Memos
        - A Payment can be created as unapplied to any Invoice or Credit Memo, in which case it is recorded as a credit.
        - If any element in any line needs to be updated, all the Lines of a Payment have to be provided. This is true
            for full or sparse update. Lines can be updated only ALL or NONE.
        - To remove all lines, send an empty Lines tag.
        - To remove some of the lines, send all the Lines that need to be present MINUS the lines that need to
            be removed.
        - To add some lines, send all existing and new Lines that need to be present.
        - The sequence in which the Lines are received is the sequence in which lines are preserved.
    """

    class_dict = {
        "CustomerRef": Ref,
        "PaymentMethodRef": Ref,
    }

    list_dict = {
        "Line": PaymentLine
    }

    qbo_object_name = "Payment"

    def __init__(self):
        self.PaymentRefNum = 0
        self.TotalAmt = 0
        self.UnappliedAmt = 0
        self.TxnDate = ""
        self.CustomerRef = None
        self.PaymentMethodRef = None
        self.Line = []

