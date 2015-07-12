from base import QuickbooksBaseObject, Address, PhoneNumber, EmailAddress, WebAddress, Ref


class Customer(QuickbooksBaseObject):
    """
    QBO definition: A customer is a consumer of the service or product that your business offers. The Customer object
    allows you to categorize customers according to your business requirements. You must first create a customer
    and then create a job referencing that customer as a parent with the ParentRef attribute. Some areas a
    sub-customer/job can be used include:

      -To track a job for the top-level customer, such as a kitchen remodel or bathroom remodel.
      -Members of a team or league.
      -Properties managed by a Homeowner Association or Property Management Company.
    """

    class_dict = {
        "BillAddr": Address,
        "ShipAddr": Address,
        "PrimaryPhone": PhoneNumber,
        "AlternatePhone": PhoneNumber,
        "Mobile": PhoneNumber,
        "Fax": PhoneNumber,
        "PrimaryEmailAddr": EmailAddress,
        "WebAddr": WebAddress,
        "DefaultTaxCodeRef": Ref,
        "SalesTermRef": Ref,
        "PaymentMethodRef": Ref
    }

    qbo_object_name = "Customer"

    def __init__(self):
        self.Title = ""
        self.GivenName = ""
        self.MiddleName = ""
        self.FamilyName = ""
        self.Suffix = ""
        self.FullyQualifiedName = ""
        self.CompanyName = ""
        self.DisplayName = ""
        self.PrintOnCheckName = ""
        self.Notes = ""
        self.Active = True
        self.Job = False
        self.BillWithParent = False
        self.Taxable = True
        self.Balance = 0
        self.BalanceWithJobs = 0
        self.PreferredDeliveryMethod = ""
        self.ResaleNum = ""

        self.BillAddr = None
        self.ShipAddr = None
        self.PrimaryPhone = None
        self.Mobile = None
        self.Fax = None
        self.PrimaryEmailAddr = None
        self.WebAddr = None
        self.DefaultTaxCodeRef = None
        self.SalesTermRef = None
        self.PaymentMethodRef = None

    def __unicode__(self):
        return self.DisplayName
