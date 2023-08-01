import quickbooks
from quickbooks.objects.account import Account


class AccountDTO:
    def __init__(self, account: quickbooks.objects.account):
        self.name = account.Name
        self.classification = account.Classification
        self.currency_ref = account.CurrencyRef.__dict__
        self.account_type = account.AccountType
        self.active = account.Active
        self.current_balance = account.CurrentBalance
