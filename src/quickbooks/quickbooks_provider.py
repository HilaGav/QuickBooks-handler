from src.common.models.account_model import AccountModel
import quickbooks.objects.account
from quickbooks import QuickBooks
import json


class QuickBooksProvider:
    def __init__(self, quickbooks_client: QuickBooks, account: quickbooks.objects.account.Account):
        self.account = account
        self.quickbooks_client = quickbooks_client

    def get_accounts(self):
        if self.quickbooks_client is None:
            return None
        accounts = self.account.all(qb=self.quickbooks_client)
        accounts_modeling = [AccountModel(account.Name, account.Classification, account.CurrencyRef, account.AccountType
                                          , account.Active, account.CurrentBalance).__dict__ for account in accounts]
        return json.dumps(accounts_modeling)
