from base import QuickbooksBaseObject, Ref, LinkedTxn, QuickbooksManagedObject, QuickbooksTransactionEntity, \
    LinkedTxnMixin
from tax import TxnTaxDetail


class MarkupInfo(QuickbooksBaseObject):
    class_dict = {
        "PriceLevelRef": Ref,
    }

    def __init__(self):
        super(MarkupInfo, self).__init__()
        self.PercentBased = False
        self.Value = 0
        self.Percent = 0
        self.PriceLevelRef = None


class AccountBasedExpenseLineDetail(QuickbooksBaseObject):
    class_dict = {
        "CustomerRef": Ref,
        "AccountRef": Ref,
        "TaxCodeRef": Ref,
        "ClassRef": Ref,
        "MarkupInfo": MarkupInfo,
    }

    def __init__(self):
        super(AccountBasedExpenseLineDetail, self).__init__()
        self.BillableStatus = ""
        self.TaxAmount = 0
        self.TaxInclusiveAmt = 0

        self.CustomerRef = None
        self.AccountRef = None
        self.TaxCodeRef = None

    def __unicode__(self):
        return self.BillableStatus


class ItemBasedExpenseLineDetail(QuickbooksBaseObject):
    class_dict = {
        "ItemRef": Ref,
        "ClassRef": Ref,
        "PriceLevelRef": Ref,
        "TaxCodeRef": Ref,
        "CustomerRef": Ref,
        "MarkupInfo": MarkupInfo
    }

    def __init__(self):
        super(ItemBasedExpenseLineDetail, self).__init__()
        self.BillableStatus = ""
        self.UnitPrice = 0
        self.TaxInclusiveAmt = 0
        self.Qty = 0
        self.ItemRef = None
        self.ClassRef = None
        self.PriceLevelRef = None
        self.TaxCodeRef = None
        self.MarkupInfo = None
        self.CustomerRef = None


class BillLine(QuickbooksBaseObject):
    class_dict = {
        "AccountBasedExpenseLineDetail": AccountBasedExpenseLineDetail,
        "ItemBasedExpenseLineDetail": ItemBasedExpenseLineDetail,
    }

    list_dict = {
        "LinkedTxn": LinkedTxn
    }

    def __init__(self):
        super(BillLine, self).__init__()

        self.Id = 0
        self.LineNum = 0
        self.Description = ""
        self.Amount = ""
        self.DetailType = "AccountBasedExpenseLineDetail"

        self.AccountBasedExpenseLineDetail = None
        self.ItemBasedExpenseLineDetail = None

    def __unicode__(self):
        return str(self.Amount)


class Bill(QuickbooksManagedObject, QuickbooksTransactionEntity, LinkedTxnMixin):
    """
    QBO definition: A Bill entity is an AP transaction representing a request-for-payment from a third party for
    goods/services rendered and/or received.
    """

    class_dict = {
        "SalesTermRef": Ref,
        "CurrencyRef": Ref,
        "APAccountRef": Ref,
        "VendorRef": Ref,
        "AttachableRef": Ref,
        "DepartmentRef": Ref,
        "TxnTaxDetail": TxnTaxDetail,
    }

    list_dict = {
        "Line": BillLine,
        "LinkedTxn": LinkedTxn
    }

    qbo_object_name = "Bill"

    def __init__(self):
        super(Bill, self).__init__()

        self.DueDate = ""
        self.Balance = 0
        self.TotalAmt = ""
        self.TxnDate = ""
        self.DocNumber = ""
        self.PrivateNote = ""
        self.ExchangeRate = 0
        self.GlobalTaxCalculation = ""

        self.SalesTermRef = None
        self.CurrencyRef = None
        self.AttachableRef = None
        self.VendorRef = None
        self.DepartmentRef = None
        self.APAccountRef = None

        self.LinkedTxn = []
        self.Line = []

    def __unicode__(self):
        return str(self.Balance)
