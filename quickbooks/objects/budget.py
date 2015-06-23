from base import QuickbooksBaseObject, Ref


class Budget(QuickbooksBaseObject):
    """
    QBO definition: The Budget endpoint allows you to retrieve the current state of budgets already set up in the user's
    company file. A budget allows for an amount to be assigned on a monthly, quarterly, or annual basis for a specific
    account or customer and are created to give a business measurable expense goals. This amount represents how much
    should be spent against that account or customer in the give time period.
    """

    class_dict = {
        "BudgetDetail": BudgetDetail,
    }

    qbo_object_name = "Budget"

    def __init__(self):
        self.Name = ""
        self.StartDate = ""
        self.EndDate = ""
        self.BudgetType = ""
        self.BudgetEntryType = ""
        self.Active = True

        self.BudgetDetail = None

    def __unicode__(self):
        return self.Name


class BudgetDetail(QuickbooksBaseObject):
    class_dict = {
        "AccountRef": Ref,
        "CustomerRef": Ref
    }

    def __init__(self):
        self.BudgetDate = ""
        self.Amount = 0

        self.AccountRef = None
        self.CustomerRef = None

    def __unicode__(self):
        return self.Amount