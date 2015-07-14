from ..mixins import ToJsonMixin, FromJsonMixin, ReadMixin, ListMixin, UpdateMixin



class QuickbooksBaseObject(ToJsonMixin, FromJsonMixin):
    def __init__(self):
        self.Id = 0
        self.SyncToken = 0
        self.sparse = "false"
        self.domain = "QBO"
        self.TxnDate = ""


class QuickbooksManagedObject(QuickbooksBaseObject, ReadMixin, ListMixin, UpdateMixin):
    pass


class MetaData:
    def __init__(self):
        self.CreateTime = ""
        self.LastUpdatedTime = ""


class Address(ToJsonMixin, FromJsonMixin):
    def __init__(self):
        self.Id = 0
        self.Line1 = ""
        self.Line2 = ""
        self.City = ""
        self.CountrySubDivisionCode = ""
        self.PostalCode = ""
        self.Lat = ""
        self.Long = ""

    def __unicode__(self):
        return "{0} {1}, {2} {3}".format(self.Line1, self.City, self.CountrySubDivisionCode, self.PostalCode)


class PhoneNumber(ToJsonMixin, FromJsonMixin):
    def __init__(self):
        self.FreeFormNumber = ""

    def __unicode__(self):
        return self.FreeFormNumber


class EmailAddress(ToJsonMixin, FromJsonMixin):
    def __init__(self):
        self.Address = ""

    def __unicode__(self):
        return self.Address


class WebAddress(ToJsonMixin, FromJsonMixin):
    def __init__(self):
        self.URI = ""

    def __unicode__(self):
        return self.URI


class Ref(ToJsonMixin, FromJsonMixin):
    def __init__(self):
        self.value = ""
        self.name = ""

    def __unicode__(self):
        return self.name


class CustomField(ToJsonMixin, FromJsonMixin):
    def __init__(self):
        self.Type = ""
        self.Name = ""
        self.StringValue = ""

    def __unicode__(self):
        return self.Name


class LinkedTxn(QuickbooksBaseObject):
    qbo_object_name = "LinkedTxn"

    def __init__(self):
        self.TxnId = 0
        self.TxnType = 0
        self.TxnLineId = 0


class CustomerMemo(QuickbooksBaseObject):
    def __init__(self):
        self.Value = ""

    def __unicode__(self):
        return self.Value
