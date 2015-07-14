from base import QuickbooksBaseObject, Ref, QuickbooksManagedObject


class TaxLineDetail(QuickbooksBaseObject):
    class_dict = {
        "TaxRateRef": Ref
    }

    def __init__(self):
        super(TaxLineDetail, self).__init__()
        self.PercentBased = True
        self.TaxPercent = 0
        self.NetAmountTaxable = 0


class TaxLine(QuickbooksBaseObject):
    class_dict = {
        "TaxLineDetail": TaxLineDetail
    }

    def __init__(self):
        super(TaxLine, self).__init__()
        self.Amount = 0
        self.DetailType = ""


class TxnTaxDetail(QuickbooksManagedObject):
    class_dict = {
        "TxnTaxCodeRef": Ref,
    }

    list_dict = {
        "TaxLine": TaxLine
    }

    def __init__(self):
        super(TxnTaxDetail, self).__init__()
        self.TotalTax = 0
        self.TxnTaxCodeRef = None
        self.TaxLine = []
